try:
    my_file = open('apache_logs.txt', "r")
except FileNotFoundError:
    print("apache_logs.txt not found")
except IOError:
    print("apache_logs.txt could not be read")
result_dict = {}
for line in my_file:
    print(line)
    my_list = line.split(" ")
    print(my_list)
    print(my_list[8])
    if my_list[8] in result_dict:
        result_dict[my_list[8]] += 1
    else:
        result_dict[my_list[8]] = 1
    #break
print(result_dict)
