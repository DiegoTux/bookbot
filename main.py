from stats import count_words
from stats import count_characters


def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return book_content
    
def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    count_words(get_book_text("books/frankenstein.txt"))
    print("--------- Character Count -------")
    temp_var = count_characters(get_book_text("books/frankenstein.txt"))
    #temp_var.sort()
    # print(type(temp_var))
    print(temp_var)
main()