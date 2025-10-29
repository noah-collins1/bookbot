def get_num_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text):
    count_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1
    return count_dict
