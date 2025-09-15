import sys
from stats import count_words
from stats import count_chars
from stats import sorted_char_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(count_words())
    print("-------- Character Count --------")
    for item in sorted_char_count(count_chars()):
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")

    
