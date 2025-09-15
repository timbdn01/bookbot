import sys
char_count = {}

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def get_text():
    book_text = get_book_text(sys.argv[1])
    return(book_text)
def count_words():
    text = get_text()
    words = text.split()
    count = len(words)
    return(f"Found {count} total words")
def count_chars():
    text = get_text()
    text = text.lower()
    for char in text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return(char_count)
def sorted_char_count(input):
    sorted_list = sorted(input.items(), key=lambda item: item[1], reverse=True)
    return(sorted_list)

