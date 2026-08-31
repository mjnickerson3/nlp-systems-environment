"""
Tokenizer Assignment - Starter Template
Name: _Mandi Schmuhl____________
Date: __08/31/2026_________

Instructions:
- Complete each function where indicated with TODO comments.
- Do NOT delete function definitions.
- You may add helper functions if needed.
"""
import re
from collections import Counter

def read_text_file(filename):
    """
    Read and return the contents of a text file.
    """
    # TODO: Open the file and return its contents
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def whitespace_tokenize(text):
    """
    Tokenize text using whitespace only.
    Example:
    "Hello world!" -> ["Hello", "world!"]
    """
    # TODO: Split text on whitespace
    tokens = text.split()
    return tokens


def preprocess_contractions(text):
    """
    OPTIONAL (Recommended):
    Separate common contractions like:
    don't -> do n't
    I'm -> I 'm
    Hint: Use re.sub()
    """
    # TODO: Apply at least 2 contraction rules
    text = re.sub(r"don't", "do n't", text)
    text = re.sub(r"I'm", "I 'm", text)
    return text


def regex_tokenize(text):
    """
    Tokenize text using regular expressions.
    Your tokenizer MUST handle:
    - punctuation (separate it)
    - numbers (keep decimals like 12.50 together)
    - contractions (after preprocessing)
    CHALLENGE:
    - Handle URLs OR emails OR hyphenated words
    """
    # OPTIONAL: Call contraction preprocessing
    text = preprocess_contractions(text)

    # TODO: Write your regex pattern
    # Example starting point (you should improve this):
    pattern = r"[A-Za-z]+(?:-[A-Za-z]+)+|[A-Za-z]+(?:'[A-Za-z]+)?|\d+\.\d+|\d+|[^\w\s]"

    # TODO: Use re.findall() to extract tokens
    tokens = re.findall(pattern, text)
    return tokens


def token_statistics(tokens):
    """
    Return:
    - total number of tokens
    - number of unique tokens
    - frequency counts
    """
    # TODO: Compute statistics
    total = len(tokens)
    unique = len(set(tokens))
    frequencies = Counter(tokens)
    return total, unique, frequencies


def print_token_report(name, tokens):
    """
    Print:
    - total tokens
    - unique tokens
    - first 20 tokens
    """
    # TODO: Call token_statistics()
    total, unique, frequencies = token_statistics(tokens)

    print(f"\n=== {name} ===")
    print(f"Total tokens: {total}")
    print(f"Unique tokens: {unique}")

    # TODO: Print first 20 tokens
    print("First 20 tokens:", tokens[:20])

    # TODO (Optional): Print top 5 most common tokens
    print("Top 5 most common:", frequencies.most_common(5))


def compare_tokenizers(tokens1, tokens2):
    """
    Compare two token lists.
    """
    print("\n=== Comparison ===")

    # TODO: Print total tokens for each
    print("Tokenizer 1 total:", len(tokens1))
    print("Tokenizer 2 total:", len(tokens2))

    # TODO: Print unique token counts
    print("Tokenizer 1 unique:", len(set(tokens1)))
    print("Tokenizer 2 unique:", len(set(tokens2)))

    # TODO: Show example differences (first 10 tokens from each)
    print("\nTokenizer 1 sample:", tokens1[:10])
    print("Tokenizer 2 sample:", tokens2[:10])


def main():
    # Change this to the file you will provide
    filename = "sample_text.txt"

    try:
        text = read_text_file(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    # Run both tokenizers
    whitespace_tokens = whitespace_tokenize(text)
    regex_tokens = regex_tokenize(text)

    # Print reports
    print_token_report("Whitespace Tokenizer", whitespace_tokens)
    print_token_report("Regex Tokenizer", regex_tokens)

    # Compare results
    compare_tokenizers(whitespace_tokens, regex_tokens)


if __name__ == "__main__":
    main()