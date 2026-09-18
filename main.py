import os
import sys
from stats import word_splicer
from stats import character_count
from stats import chars_dict_to_sorted_list


def get_book_text(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        file_contents: str = f.read()
    return file_contents


def print_report(path: str, number_of_words:int, sorted_output: list[tuple[str,int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    for char, count in sorted_output:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

    print("============= END ===============")




def main()->None:
    if len(sys.argv[1:]) == 0:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path: str = sys.argv[1]
        text:str = get_book_text(book_path)
        number_of_words:int = word_splicer(text)
        chars:dict[str,int] = character_count(text)
        sorted_output = chars_dict_to_sorted_list(chars)
        print_report(book_path, number_of_words, sorted_output)





main()
