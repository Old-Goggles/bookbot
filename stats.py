def total_words(text):
    return len(text.split())

def character_totals(text):
    text = text.lower()
    letters = {}
    for letter in text:
        letters[letter] = letters.get(letter, 0) + 1
    return letters

def sort_chars(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict_item):
    return dict_item["count"]  
