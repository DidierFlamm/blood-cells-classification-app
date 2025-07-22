import time
import json
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy.ndimage import uniform_filter, gaussian_filter1d
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account


# stream function
def stream_data(text, word_by_word=False, sleep=0.03):
    if word_by_word:
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.1)
    else:
        for char in text:
            yield char
            time.sleep(sleep)


# Get Google credentials from st.secrets (Streamlit Cloud)
if "google_credentials" in st.secrets:
    creds_attrdict = st.secrets["google_credentials"]
    creds_dict = dict(creds_attrdict)
    # Create JSON string from dict
    creds_json = json.dumps(creds_dict)
    # Load Google credentials from JSON string
    credentials = service_account.Credentials.from_service_account_info(
        json.loads(creds_json)
    )
    translate_client = translate.Client(credentials=credentials)
else:

    st.warning(
        "Traduction won't work because google_credentials was not found in st.secrets. Please add it to your .streamlit/secrets.toml or app settings.",
        icon="🔒",
    )


# translation function using Google Cloud Translation API
@st.cache_data
def translate_text(text: str, language: str):
    if "google_credentials" in st.secrets and not language.startswith(
        "en"
    ):  # do not translate if language is 'en'
        return translate_client.translate(text, target_language=language)[
            "translatedText"
        ]
    else:
        return text


# translate and write text
@st.cache_data
def trans_write(text, language):
    text = translate_text(text, language)
    st.write(text)


def threshold_otsu(image, nbins=256):
    hist, bin_edges = np.histogram(image.ravel(), bins=nbins)
    hist = hist.astype(float)
    hist /= hist.sum()

    cumsum = np.cumsum(hist)
    cummean = np.cumsum(hist * np.arange(nbins))
    mean_total = cummean[-1]

    numerator = (mean_total * cumsum - cummean) ** 2
    denominator = cumsum * (1 - cumsum)
    with np.errstate(divide="ignore", invalid="ignore"):
        sigma_b_squared = numerator / denominator
        sigma_b_squared[denominator == 0] = 0

    idx = np.argmax(sigma_b_squared)
    return bin_edges[idx]


def threshold_yen(image, nbins=256):
    image = image.ravel()
    hist, bin_edges = np.histogram(image, bins=nbins, range=(0, 1))
    hist = hist.astype(np.float64)
    hist_norm = hist / hist.sum()

    p1_sq = np.cumsum(hist_norm**2)
    p2_sq = np.cumsum(hist_norm[::-1] ** 2)[::-1]

    with np.errstate(divide="ignore", invalid="ignore"):
        criterion = np.log(p1_sq[:-1] * p2_sq[1:])
    threshold_idx = np.argmax(criterion)

    t = (bin_edges[threshold_idx] + bin_edges[threshold_idx + 1]) / 2
    return t


def threshold_niblack(image, window_size=15, k=0.2):
    image = image.astype(float)
    mean = uniform_filter(image, window_size)
    mean_sq = uniform_filter(image**2, window_size)
    std = np.sqrt(mean_sq - mean**2)
    return mean + k * std


def threshold_sauvola(image, window_size=15, k=0.2, r=128):
    image = image.astype(float)
    mean = uniform_filter(image, window_size)
    mean_sq = uniform_filter(image**2, window_size)
    std = np.sqrt(mean_sq - mean**2)
    return mean * (1 + k * ((std / r) - 1))


class ImagesBinarizer:
    """
    Binarizes image datasets using a fixed or computed threshold.

    Methods:
        fit(X):                     Compute global Otsu and Yen thresholds.
        transform(X):               Apply binarization using the selected threshold.
        fit_transform(X):           Fit then transform.
        plot_threshold_analysis(X): Plot intensity distribution with threshold lines.
        show_samples(X, n_samples): Plot random binarized images.
        to_grayscale(X):            Convert a batch of images into grayscale images.

    Supports RGB, grayscale (2D/3D), and flattened (1D) images.
    """

    def __init__(self, threshold: float | str = 0.5):
        """
        Parameters:
            threshold: str or float
                'otsu', 'yen', 'niblack', 'sauvola' or float value for fixed threshold.
        """

        self.threshold_param = threshold
        self.otsu_ = None
        self.yen_ = None
        self.threshold_ = None

    def to_grayscale(self, X) -> np.ndarray:
        """
        Convert a batch of images (RGB, grayscale 2D/3D, or flattened 1D)
        into grayscale images:
          - flattened 1D images if input images are flattened,
          - 2D grayscale images otherwise.
        """
        X = np.asarray(X)

        if X.ndim == 2:  # batch of flatten 1D images (n_samples, pixels)
            return X

        elif X.ndim == 3:
            if (
                X.shape[-1] == 1
            ):  # batch of flattened images with a trailing 1 channel dim (n_samples, pixels, 1)
                return X.squeeze(axis=-1)
            else:
                return X  # batch of 2D grayscale images (n_samples, H, W)

        elif X.ndim == 4:
            if (
                X.shape[-1] == 1
            ):  # batch of 3D grayscale images (n_samples, height, width, 1) → flatten last dim
                return X.squeeze(axis=-1)
            elif X.shape[-1] == 3:  # batch of RGB images, convert each to grayscale 2D
                gray_images = [
                    0.2989 * img[..., 0] + 0.5870 * img[..., 1] + 0.1140 * img[..., 2]
                    for img in X
                ]  # 0.2989 * R + 0.5870 * G + 0.1140 * B are the real Rec. 601 luminance weights used by skimage.color.rgb2gray()
                return np.array(
                    gray_images
                )  # human eyes are more sensitive to green, then to red, and finally to blue.
            else:
                raise ValueError(f"Unexpected image shape: {X.shape[-1]}")

        else:
            raise ValueError(f"Unexpected input array dimensions: {X.ndim}")

    def fit(self, X, y=None) -> "ImagesBinarizer":
        """
        Compute global Otsu and Yen thresholds for the training set
        and estimate global-equivalent Niblack and Sauvola thresholds
        by computing the median of local thresholds (ie median of pixel threshold) per images

        Parameters:
            X : array-like
                Batch of images (RGB, grayscale, or flattened) with shape
                (n_samples, ...) and pixel values in [0,255] or [0,1].
            y: Ignored (scikit-learn convention)

        Returns:
            self : fitted ImagesBinarizer
        """

        X = np.asarray(X)

        # Accept 2D, 3D or 4D datasets
        if X.ndim not in [2, 3, 4]:
            raise ValueError(
                f"Expected 2D, 3D or 4D array, got {X.ndim}D array instead."
            )

        if X.min() < 0:
            raise ValueError(
                "Pixel values contain negatives, please check data preprocessing."
            )

        if X.max() > 1:
            X = X / 255.0  # Normalize pixels to [0,1]

        X_gray = self.to_grayscale(X)  # 2D or 3D

        # Compute global Otsu and Yen thresholds
        gray_pixels = X_gray.ravel()
        self.otsu_ = threshold_otsu(gray_pixels)
        self.yen_ = threshold_yen(gray_pixels)

        print(f"Otsu threshold = {self.otsu_}")
        print(f"Yen threshold  = {self.yen_}")

        if self.threshold_param == "otsu":
            self.threshold_ = self.otsu_
        elif self.threshold_param == "yen":
            self.threshold_ = self.yen_
        else:
            self.threshold_ = (
                self.threshold_param
            )  # can be a global float or a local method name

        return self

    def transform(self, X) -> np.ndarray:
        """
        Binarize a batch of images using global (fixed or computed during fit float) or local (str) threshold.

        Parameters:
            X : array-like
                Batch of images (RGB, grayscale, or flattened) with pixel values in [0, 255] or [0, 1].

        Returns:
            np.ndarray
                Binarized images with pixel values 0 or 1.
        """

        # Vérifie que fit a été exécuté avant transform
        if self.threshold_ is None:
            raise RuntimeError("You must fit the transformer before calling transform.")

        X = np.asarray(X)

        # Accept 2D, 3D or 4D datasets
        if X.ndim not in [2, 3, 4]:
            raise ValueError(
                f"Expected 2D, 3D or 4D array, got {X.ndim}D array instead."
            )

        if X.min() < 0:
            raise ValueError("Pixel values contain negatives.")

        if (
            X.max() > 1
        ):  # normalise si besoin pour être compatible avec le seuil entre 0 et 1
            X = X / 255.0

        X_gray = self.to_grayscale(X)

        # Binarization selon le seuil en pixel 0 ou 1
        # self.threshold_ peut être soit un float (seuil global) soit un str (méthode adaptative)

        if isinstance(self.threshold_, str):  # seuil local
            X_bin = []
            for img in X_gray:
                if self.threshold_ == "niblack":
                    thresh_local = threshold_niblack(img)
                elif self.threshold_ == "sauvola":
                    thresh_local = threshold_sauvola(img)
                else:
                    raise ValueError(
                        f"Invalid local threshold method: {self.threshold_}"
                    )
                binary_img = img > thresh_local
                X_bin.append(binary_img)
            return np.array(X_bin)
        else:  # seuil global
            return (X_gray > self.threshold_).astype(np.uint8)

    def fit_transform(self, X, y=None):
        """
        Fit to data, then transform it.

        Parameters:
            X : array-like
                Batch of images to binarize.
            y: Ignored (scikit-learn convention)

        Returns:
            np.ndarray
                Binarized images as uint8 arrays (0 or 1).
        """

        return self.fit(X, y).transform(X)

    def plot_threshold_analysis(self, X):
        """
        Display grayscale histogram with global threshold lines and RGB curves if applicable.

        Parameters:
            X : array-like
                Batch of images (RGB, grayscale, or flattened).
        """

        if self.otsu_ is None or self.yen_ is None:
            raise RuntimeError(
                "You must fit the transformer before calling plot_threshold_analysis"
            )

        X = np.asarray(X)

        # Accept 2D, 3D or 4D datasets
        if X.ndim not in [2, 3, 4]:
            raise ValueError(
                f"Expected 2D, 3D or 4D array, got {X.ndim}D array instead."
            )

        if X.min() < 0:
            raise ValueError("Pixel values contain negatives.")

        if X.max() > 1:
            X = (
                X / 255.0
            )  # normalise si besoin pour afficher des intensités entre 0 et 1

        if X.ndim == 4:
            plt.figure(figsize=(8, 4))

            for i in tqdm(range(3), desc="Computing RGB colorimetry"):
                channel_i_pixels = X[:, :, :, i].ravel()
                hist, bins = np.histogram(channel_i_pixels, bins=256, range=(0, 1))
                hist_smooth = gaussian_filter1d(hist, sigma=2)
                bin_centers = (bins[:-1] + bins[1:]) / 2
                plt.plot(bin_centers, hist_smooth, color=["red", "green", "blue"][i])

            plt.title("Grayscale & RGB Distribution with Thresholds")

            plt.xlabel("Intensity")
            plt.ylabel("Pixel count")
            plt.tight_layout()

        X_gray = self.to_grayscale(X)

        # histogram luminance
        gray_pixels = X_gray.ravel()
        plt.hist(gray_pixels, bins=256, color="gray", alpha=0.7)

        # If a custom threshold, show it too in red
        if isinstance(self.threshold_param, float):
            plt.axvline(
                self.threshold_param,
                color="purple",
                linestyle="--",
                label=f"Custom = {self.threshold_}",
            )

        # Computed threshold lines
        plt.axvline(
            self.otsu_,
            color="orange",
            linestyle=":",
            label=f"Otsu (from fit) = {self.otsu_:.3f}",
        )
        plt.axvline(
            self.yen_,
            color="brown",
            linestyle=":",
            label=f"Yen (from fit) = {self.yen_:.3f}",
        )

        plt.legend()

        plt.xlabel("Intensity")
        plt.ylabel("Pixel count")
        plt.tight_layout()
        plt.show()

    def show_sample(self, X, y=None, names=None):

        if self.otsu_ is None:
            raise RuntimeError("You must fit the transformer before calling show")

        X = np.asarray(X)

        # Accept 2D, 3D or 4D datasets
        if X.ndim not in [2, 3, 4]:
            raise ValueError(
                f"Expected 2D, 3D or 4D array, got {X.ndim}D array instead."
            )

        # Choisis 1 image au hasard
        idx = np.random.randint(len(X))
        img = X[idx]

        if img.min() < 0:
            raise ValueError("Pixel values contain negatives.")

        if img.max() > 1:
            img = (
                img / 255.0
            )  # normalise si besoin pour afficher des intensités entre 0 et 1

        img_gray = self.to_grayscale((img,))[0]
        img_bin = self.transform((img,))[0]

        fig, axs = plt.subplots(4, 5, figsize=(15, 12))

        # original
        axs[0, 0].imshow(img)
        axs[0, 0].axis("off")
        title = f"#{idx}"
        if y is not None:
            title += f" ({y[idx]})"
        if names is not None:
            title += f"\n{names[idx]}"
        axs[0, 0].set_title(title)

        # grayscale
        axs[0, 1].imshow(img_gray, cmap="gray")
        axs[0, 1].axis("off")
        axs[0, 1].set_title("grayscale")

        # RGB
        for i in range(3):
            img_i = img[:, :, i]
            axs[0, i + 2].imshow(img_i, cmap=["Reds_r", "Greens_r", "Blues_r"][i])
            axs[0, i + 2].axis("off")
            axs[0, i + 2].set_title(f"{['R channel', 'G channel', 'B channel'][i]}")

        # custom
        axs[1, 0].imshow(img_bin, cmap="gray", vmin=0, vmax=1)
        axs[1, 0].axis("off")
        axs[1, 0].set_title(f"custom = {self.threshold_param}")

        threshold_origin = self.threshold_
        # computed

        self.threshold_ = self.otsu_
        img_bin = self.transform((img,))[0]
        axs[1, 1].imshow(img_bin, cmap="gray", vmin=0, vmax=1)
        axs[1, 1].axis("off")
        axs[1, 1].set_title(f"Otsu (from fit) = {self.threshold_:.3f}")

        self.threshold_ = self.yen_
        img_bin = self.transform((img,))[0]
        axs[1, 2].imshow(img_bin, cmap="gray", vmin=0, vmax=1)
        axs[1, 2].axis("off")
        axs[1, 2].set_title(f"Yen (from fit) = {self.threshold_:.3f}")

        niblack_thresh = threshold_niblack(img_gray)
        niblack_img = img_gray > niblack_thresh
        axs[1, 3].imshow(niblack_img, cmap="gray", vmin=0, vmax=1)
        axs[1, 3].axis("off")
        axs[1, 3].set_title("Niblack")

        sauvola_thresh = threshold_sauvola(img_gray)
        sauvola_img = img_gray > sauvola_thresh
        axs[1, 4].imshow(sauvola_img, cmap="gray", vmin=0, vmax=1)
        axs[1, 4].axis("off")
        axs[1, 4].set_title("Sauvola")

        # range
        for i in range(9):
            row = i // 5 + 2
            col = i % 5
            self.threshold_ = (i + 1) / 10
            img_bin = self.transform((img,))[0]
            axs[row, col].imshow(img_bin, cmap="gray", vmin=0, vmax=1)
            axs[row, col].axis("off")
            axs[row, col].set_title(f"threshold = {self.threshold_:.1f}")

        self.threshold_ = threshold_origin

        # threshold analysis
        pixels_gray = img_gray.ravel()
        axs[3, 4].hist(pixels_gray, bins=256, color="gray", alpha=0.7)
        axs[3, 4].axvline(
            self.otsu_,
            color="orange",
            linestyle=":",
            label=f"Otsu (fit) = {self.otsu_:.3f}",
        )
        axs[3, 4].axvline(
            self.yen_,
            color="brown",
            linestyle=":",
            label=f"Yen (fit) = {self.yen_:.3f}",
        )
        if isinstance(threshold_origin, float):
            axs[3, 4].axvline(
                threshold_origin,
                color="purple",
                linestyle="--",
                label=f"custom = {threshold_origin}",
            )
            axs[3, 4].legend()
        axs[3, 4].set_xlabel("Intensity")
        axs[3, 4].set_ylabel("Pixel count")
        for i in range(3):
            pixels_i = img[:, :, i].ravel()
            hist, bins = np.histogram(pixels_i, bins=256, range=(0, 1))
            hist_smooth = gaussian_filter1d(hist, sigma=2)
            bin_centers = (bins[:-1] + bins[1:]) / 2
            axs[3, 4].plot(bin_centers, hist_smooth, color=["red", "green", "blue"][i])

        plt.tight_layout()
        plt.show()
