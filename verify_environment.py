"""
NLP Environment Setup Verification

This script verifies that the required libraries for the course
are installed and can be imported successfully.
"""

import sys


def check_import(module_name: str, import_statement):
    """
    Run an import check and print the result.
    """
    try:
        import_statement()
        print(f"[OK] {module_name} imported successfully")
    except Exception as e:
        print(f"[ERROR] {module_name} failed to import: {e}")


def main():
    print("NLP Environment Setup Verification")
    print("-" * 40)
    print(f"Python version: {sys.version}")
    print("-" * 40)

    check_import("numpy", lambda: __import__("numpy"))
    check_import("pandas", lambda: __import__("pandas"))
    check_import("matplotlib", lambda: __import__("matplotlib"))
    check_import("scikit-learn", lambda: __import__("sklearn"))
    check_import("nltk", lambda: __import__("nltk"))
    check_import("torch", lambda: __import__("torch"))
    check_import("transformers", lambda: __import__("transformers"))
    check_import("datasets", lambda: __import__("datasets"))
    check_import("sentencepiece", lambda: __import__("sentencepiece"))
    check_import("librosa", lambda: __import__("librosa"))
    check_import("pyttsx3", lambda: __import__("pyttsx3"))
    check_import("openai-whisper", lambda: __import__("whisper"))

    print("-" * 40)
    print("Environment verification complete.")
    print("If all libraries show [OK], your setup is ready.")


if __name__ == "__main__":
    main()