import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# # Download required NLTK resources
# nltk.download("stopwords")
# nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """
    Clean and preprocess text using:
    - Lowercase conversion
    - Special character removal
    - Stopword removal
    - Lemmatization
    """

    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Tokenization
    words = text.split()

    # Remove stopwords and apply lemmatization
    processed_words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(processed_words)


if __name__ == "__main__":

    sample_text = """
    Artificial Intelligence and Machine Learning are used
    to build intelligent applications.
    """

    processed_text = preprocess_text(sample_text)

    print("\n===== NLP PREPROCESSING =====")
    print("Original Text:")
    print(sample_text)

    print("\nProcessed Text:")
    print(processed_text)