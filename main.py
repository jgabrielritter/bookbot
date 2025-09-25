import sys
from stats import get_num_words, get_char_counts, sort_char_counts


def get_book_text(filepath):
    """
    Read the contents of a file and return it as a string.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main():
    # Check for correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    # Read the book text
    book_text = get_book_text(filepath)

    # Word count
    num_words = get_num_words(book_text)

    # Character counts
    char_counts = get_char_counts(book_text)
    sorted_chars = sort_char_counts(char_counts)

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():  # only letters
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
