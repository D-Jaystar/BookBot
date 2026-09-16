import os
from stats import word_splicer
from stats import character_count



def get_book_text(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        file_contents: str = f.read()
    return file_contents























def main()->None:
    book_path: str = "books/frankenstein.txt"
    text:str = get_book_text(book_path)
    number_of_words:int = word_splicer(text)
    print(f"Found {number_of_words} total words")
    chars:dict[str,int] = character_count(text)
    print(chars)






main()
