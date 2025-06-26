from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return book_content
    
def main():
    count_words(get_book_text("books/frankenstein.txt"))
main()