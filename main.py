from stats import get_nums_words
from stats import count_letters
from stats import chars_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    book_text = get_book_text((sys.argv[1]))
    num_words = get_nums_words(book_text)
    letter_counts = count_letters(book_text)
    chars_sorted_list = chars_list(letter_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()