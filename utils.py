import time

# Fonction de stream
def stream_data(text, word_by_word=False, sleep=0.03):
    if word_by_word:
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.1)
    else:
        for char in text:
            yield char
            time.sleep(sleep)