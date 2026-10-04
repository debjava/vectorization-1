import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def without_vectorization():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    # We have to loop through each element manually
    result = []
    for i in range(len(a)):
       result.append(a[i] + b[i])
    print(result)  # Output: [6, 8, 10, 12]

def with_vectorization():
    # Convert to NumPy arrays
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])

    # Vectorized addition: applied to all elements simultaneously
    result = a + b

    print(result)  # Output: [ 6  8 10 12]

def vectorize_plain_text():
    texts = [
        "I love programming",
        "I enjoy writing software",
        "The weather is very hot today"
    ]
    model = SentenceTransformer("all-MiniLM-L6-v2")
    vectors = model.encode(texts)

    for text, vector in zip(texts, vectors):
        print(text)
        print("Dimensions:", len(vector))
        print()

def vectorization_usage1():
    sentences = [
        "The cat is sleeping.",
        "A kitten is taking a nap.",
        "The car is moving fast.",
        "THE CaT iS sleEPing"
    ]

    model = SentenceTransformer("all-MiniLM-L6-v2")
    # Convert all sentences into vectors
    vectors = model.encode(sentences)

    # Compare sentence 1 with sentence 2
    similarity = cosine_similarity(
        [vectors[0]],
        [vectors[1]]
    )

    print("Similarity:", similarity[0][0]) # Similarity: 0.71426237

    similarity = cosine_similarity(
        [vectors[0]],
        [vectors[2]]
    )
    print(similarity[0][0]) # -0.012199283

    similarity = cosine_similarity(
        [vectors[0]],
        [vectors[3]]
    )
    print(similarity[0][0])  # 0.9980756


if __name__ == '__main__':
    # without_vectorization()
    # with_vectorization()
    # vectorize_plain_text()
    vectorization_usage1()

