from stats import word_count, character_count, sorted_dict_list
import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    else:
        words = word_count(get_book_text())
        num_words = len(words)
        num_of_chars = character_count(get_book_text())
        #print(f"{len(words)} words found in the document")
        #print(num_of_chars)
        sorted_list = sorted_dict_list(num_of_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char in sorted_list:
            print(f"{char["char"]}: {char["num"]}")


main()


