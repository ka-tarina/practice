# Count letter frequency in given text


def count_letter_frequency(my_words):
    my_words = my_words.replace(" ", "")
    letter_frequency = {}
    for letter in my_words:
        keys = letter_frequency.keys()
        if letter in keys:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
    for key, value in letter_frequency.items():
        letter_frequency[key] = round((value / len(my_words))*100, 2)
    sorted_letter_frequency = sorted(letter_frequency.items())
    return sorted_letter_frequency


words = "say hello to my little friend"
print(count_letter_frequency(words))
