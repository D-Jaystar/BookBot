



def word_splicer(text:str)->int:
    words: str = text.split()
    total:int = (len(words))
    return total


def character_count(text:str)->dict[str,int]:
    char_counts: dict[str,int] = {}
    text = text.lower()
    for char in text:
       char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def chars_dict_to_sorted_list(char_counts:dict[str, int])->list[tuple[str,int]]:

    sorted_chars: list[tuple[str,int]] = []

    for letter in char_counts:
        sorted_chars.append((letter, char_counts[letter]))
    sorted_counts = sorted(sorted_chars, key=sort_on, reverse=True)
    return  sorted_counts

def sort_on(sorted_chars:tuple[str,int]) -> int:
    return sorted_chars[1]

