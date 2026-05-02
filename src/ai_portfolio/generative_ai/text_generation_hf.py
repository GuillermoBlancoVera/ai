"""Text generation example with a small Hugging Face causal language model."""

from transformers import pipeline


PROMPT = "Write a short portfolio summary for an AI engineer who works across classical ML, deep learning, and generative AI:"


def main() -> None:
    generator = pipeline(
        task="text-generation",
        model="distilgpt2",
    )

    outputs = generator(
        PROMPT,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
    )

    print("Text generation example")
    print()
    print(outputs[0]["generated_text"])


if __name__ == "__main__":
    main()
