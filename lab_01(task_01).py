def my_function(input_str):
    words_dict= {}
    for word in input_str.split():
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    return words_dict


test_string = "hello world, hello world, hello world"
print(my_function(test_string))
