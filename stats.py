def count_words(book):
    words = len(book.split())
    print(f"{words} words found in the document")

def count_characters(text):
    text = text.lower()
    count_chars = {}
    for char in text:
        if char in count_chars:
            count_chars[char] += 1
        else:
            count_chars[char] = 1 
    

def sort_items(count_chars):
    
    return count_chars
#print(count_characters)
