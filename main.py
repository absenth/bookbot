import sys
from stats import get_num_words, get_character_counts, sort_character_counts

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents


def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]


    contents = get_book_text(path)
    num_words = get_num_words(contents)
    char_count = get_character_counts(contents)
    sorted_chars = sort_character_counts(char_count)

    # Start Program Output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dict in range(len(sorted_chars)):
        print(f"{sorted_chars[dict]["char"]}: {sorted_chars[dict]["num"]}")

    print("============= END ===============")



if __name__ == "__main__":
    main()
