



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