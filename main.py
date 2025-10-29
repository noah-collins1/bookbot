import sys
from stats import get_num_words, count_characters

def get_file_path():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

file_path = get_file_path()

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        return file_contents

def sort_on(items):
    return items["count"]

def main(file_contents):
    num_words = get_num_words(file_contents)
    statement = f"Found {num_words} total words"
    char_count = count_characters(file_contents)
    char_count_list = [{"char": char, "count": count} for char, count in char_count.items()]
    char_count_list.sort(reverse=True, key=sort_on)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(statement)
    print("--------- Character Count -------")
    for item in char_count_list:
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

book_text = get_book_text(file_path)


if __name__ == "__main__":
    main(book_text)


