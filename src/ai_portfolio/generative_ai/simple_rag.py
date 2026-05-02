"""A minimal retrieval-augmented generation example."""

from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline


@dataclass(frozen=True)
class Document:
    title: str
    text: str


DOCUMENTS = [
    Document(
        title="KNN",
        text="K-nearest neighbors is a supervised learning algorithm that predicts based on nearby labeled examples.",
    ),
    Document(
        title="K-Means",
        text="K-means is an unsupervised learning algorithm that partitions data into clusters using centroid updates.",
    ),
    Document(
        title="Random Forest",
        text="Random forest is an ensemble method that combines many decision trees for classification or regression.",
    ),
]

QUESTION = "What is the difference between K-nearest neighbors and K-means?"


def retrieve_context(question: str, top_k: int = 2) -> str:
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform([doc.text for doc in DOCUMENTS] + [question])
    similarities = cosine_similarity(matrix[-1], matrix[:-1]).ravel()
    ranked_indices = similarities.argsort()[::-1][:top_k]

    return "\n".join(
        f"{DOCUMENTS[index].title}: {DOCUMENTS[index].text}"
        for index in ranked_indices
    )


def main() -> None:
    context = retrieve_context(QUESTION)

    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{QUESTION}

Answer:
""".strip()

    generator = pipeline(
        task="text2text-generation",
        model="google/flan-t5-small",
    )
    output = generator(prompt, max_new_tokens=80, do_sample=False)

    print("Simple RAG example")
    print()
    print("Retrieved context:")
    print(context)
    print()
    print("Generated answer:")
    print(output[0]["generated_text"])


if __name__ == "__main__":
    main()
