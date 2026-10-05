import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import chromadb

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

def store_vectors_in_chromadb():
    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Create/open a local Chroma database
    client = chromadb.PersistentClient(path="../../my_vector_db")

    # Create a collection
    collection = client.get_or_create_collection(name="my_documents")
    # Add new sentences
    sentences = [
        "The cat is sleeping.",
        "A kitten is taking a nap.",
        "The car is moving fast.",
        "THE CaT iS sleEPing"
    ]
    ids = [
        "doc1",
        "doc2",
        "doc3",
        "doc4"
    ]

    # Create vectors
    vectors = model.encode(sentences).tolist()

    # Store everything
    collection.add(
        ids=ids,
        documents=sentences,
        embeddings=vectors
    )

    # you can also use upsert for both new and modified records.
    # collection.upsert(
    #     ids=ids,
    #     documents=sentences,
    #     embeddings=vectors
    # )

    print("Data added successfully.")

def update_chromadb():
    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Create/open a local Chroma database
    client = chromadb.PersistentClient(path="../../my_vector_db")

    # Create a collection
    collection = client.get_or_create_collection(name="my_documents")

    updated_sentence = "The car is moving fast on the road."
    updated_vector = model.encode(updated_sentence).tolist()

    collection.update(
        ids=["doc3"],
        documents=[updated_sentence],
        embeddings=[updated_vector]
    )
    print("Data updated successfully.")

    results = collection.get(
        include=["documents", "embeddings"]
    )

    # Retrieve all documents to verify

    for doc_id, document, embedding in zip(
            results["ids"],
            results["documents"],
            results["embeddings"]
    ):
        print("=" * 50)
        print("ID       :", doc_id)
        print("Document :", document)
        # print("Vector   :", embedding)
        print("Dimensions:", len(embedding))


def query_from_chromadb():
    query = "Which animal is sleeping?"

    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_vector = model.encode(query).tolist()

    # Create/open a local Chroma database
    client = chromadb.PersistentClient(path="../../my_vector_db")

    # Create a collection
    collection = client.get_or_create_collection(name="my_documents")

    results = collection.query(
        query_embeddings=[query_vector],
        n_results=3
    )

    print(results)

    results = collection.get(
        include=["documents", "embeddings"]
    )

    documents = results["documents"]
    embeddings = results["embeddings"]

    similarities = cosine_similarity(
        [query_vector],
        embeddings
    )[0]

    for document, score in zip(documents, similarities):
        print(f"{score:.4f} -> {document}")


if __name__ == '__main__':
    # without_vectorization()
    # with_vectorization()
    # vectorize_plain_text()
    # vectorization_usage1()
    # store_vectors_in_chromadb()
    update_chromadb()
    # query_from_chromadb()

