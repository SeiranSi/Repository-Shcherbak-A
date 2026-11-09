def my_function(input_str):
    words_dict = {}
    string = input_str.replace(',', '').replace('.', '').lower()
    for word in string.split():
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    return words_dict

test_string = "hello world, hello world, hello world, hello again"
print('The string:', test_string)

result_dict = my_function(test_string)
print("Dictionary:", result_dict)

more3words = []

for word, count in result_dict.items():
    if count > 3:
        more3words.append(word)
print("Words appearing more than 3 times:", more3words)
