def get_nums_words(text):
    words = text.split()
    nums_words = len(words)
    return nums_words

def count_letters(text):
    letter_counts = {}
    for letter in text:
        if letter.isalpha():
            letter_counts[letter.lower()] = letter_counts.get(letter.lower(), 0) + 1
    return letter_counts


def sort_on(d):
    return d["num"]

def chars_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


    