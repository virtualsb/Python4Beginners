def mysplit(input_string):

    if not input_string:
        return []

    words = []

    current_word = ''

    for char in input_string:
        if char == ' ':
            if current_word:
                words.append(current_word)
                current_word = ''  
        else:
            current_word += char

    if current_word:
        words.append(current_word)

    return words


# Test cases
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit(""))
print(mysplit("abc"))