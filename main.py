from stats import count_words
from stats import count_characters
from stats import sort_items
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return book_content
    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    words = count_words(get_book_text(book_path))
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    temp_var = count_characters(get_book_text(book_path))
    char_counts = sort_items(temp_var)
    for item in char_counts:
        char = item["char"]
        amount = item["num"]
        print(f"{char}: {amount}")
    print("============= END ===============")
    # print(sys.argv)

main()