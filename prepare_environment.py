import nltk


def download_nltk_resources():
    nltk.download("punkt")
    nltk.download("wordnet")
    nltk.download("stopwords")
    nltk.download("averaged_perceptron_tagger")


if __name__ == "__main__":
    download_nltk_resources()
