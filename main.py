from stats import get_letter_count, get_word_count
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]

    word_count = get_word_count(filepath)
    letters = get_letter_count(filepath)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    for letter in letters:
        print(f"{letter["letter"]}: {letter["count"]}")

    print("============= END ===============")

main()