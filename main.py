from stats import count_words
from stats import count_characters
from stats import sort_items


def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return book_content
    
def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    temp_var = count_characters(get_book_text("books/frankenstein.txt"))
    char_counts = sort_items(temp_var)
    for item in char_counts:
        char = item["char"]
        amount = item["num"]
        print(f"{char}: {amount}")
    print("============= END ===============")

main()