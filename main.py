import os



def get_book_text(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        file_contents: str = f.read()
    return file_contents



def word_splicer(text:str)->int:
    words: str = text.split()
    total:int = (len(words))
    return total





















def main()->None:
    book_path: str = "books/frankenstein.txt"
    text:str = get_book_text(book_path)
    number_of_words:int = word_splicer(text)
    print(f"Found {number_of_words} total words")






main()
