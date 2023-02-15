from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import joblib

sentences = [
    "This is the first sentence.",
    "This is the second sentence.",
    "This is the third sentence.",
    "This is the fourth sentence."
]

reference_sentence = "This is the first sentence."

vectorizer = CountVectorizer().fit_transform(sentences + [reference_sentence])
cosine_similarities = cosine_similarity(vectorizer[-1], vectorizer[:-1]).flatten()

for i, similarity in enumerate(cosine_similarities):
    if similarity > 0.5:
        print(f"Sentence {i + 1} matches the reference sentence with a similarity of {similarity:.2f}.")
    else:
        print(f"Sentence {i + 1} does not match the reference sentence with a similarity of {similarity:.2f}.")

#In this example, the CountVectorizer class from the scikit-learn library is used to convert the sentences into a numerical representation.
#  The cosine_similarity function from the same library is used to calculate the cosine similarity between the reference sentence and each of the other sentences. 
# The cosine similarity ranges from 0, indicating no similarity, to 1, indicating a perfect match. In this example, a similarity threshold of 0.5 is used to determine
#  whether a sentence matches the reference sentence with some degree of accuracy. You can adjust this threshold to suit your needs.
