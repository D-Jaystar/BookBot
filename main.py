def get_book_text(path):
    with open(path, encoding ="utf-8") as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

main()