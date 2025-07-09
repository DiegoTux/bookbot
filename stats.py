def count_words(book):
    words = len(book.split())
    return words

def count_characters(text):
    text = text.lower()
    count_chars = {}
    for char in text:
        if char in count_chars:
            count_chars[char] += 1
        else:
            count_chars[char] = 1 
    return count_chars
    

def sort_items(count_chars):
    new_dict = []
    def sort_on(count_chars):
        return count_chars["num"]
        
    for char in count_chars:
        if char.isalpha() == True:
            new_dict.append({ "char": char, "num": count_chars[char]})
            
    new_dict.sort(key=sort_on, reverse=True)
    return new_dict