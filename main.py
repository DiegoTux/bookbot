def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        print(book_content)

def main():
    get_book_text("books/frankenstein.txt")

main()
