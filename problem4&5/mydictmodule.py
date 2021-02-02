def split_dictionary(dictionary):
    file_keys = open("keys.txt", "wt")
    file_values = open("values.txt", "wt")

    keys_list = list(dictionary.keys())
    values_list = list(dictionary.values())
    # print(keys_list)
    # print(values_list)
    # print(type(keys_list))
    # print(type(values_list))
    for i in range(len(keys_list)-1):
        file_keys.write(str(keys_list[i]) + "\n")
        file_values.write(str(values_list[i]) + "\n")

    file_keys.write(str(keys_list[-1]))
    file_values.write(str(values_list[-1]))
    file_keys.close()
    file_values.close()
