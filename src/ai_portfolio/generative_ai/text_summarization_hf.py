"""Summarization example with a small sequence-to-sequence model."""

from transformers import pipeline


TEXT = """
Large language models have changed how many AI systems are built, but shipping useful generative
AI products still requires careful work around prompting, retrieval, evaluation, latency, cost,
and failure handling. A strong portfolio should show not only model usage, but also engineering
judgment, task framing, and a clear understanding of where these systems are reliable or brittle.
"""


def main() -> None:
    summarizer = pipeline(
        task="summarization",
        model="sshleifer/distilbart-cnn-12-6",
    )

    output = summarizer(TEXT, max_length=60, min_length=20, do_sample=False)

    print("Summarization example")
    print()
    print(output[0]["summary_text"])


if __name__ == "__main__":
    main()
