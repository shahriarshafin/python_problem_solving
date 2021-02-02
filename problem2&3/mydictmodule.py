def makeDictionary(keys, values):
    file_keys = open(keys, "rt")
    file_values = open(values, "rt")

    keys_with_newline = file_keys.readlines()
    values_with_newline = file_values.readlines()
    keys = list(map(lambda x: x.strip(), keys_with_newline))
    values = list(map(lambda x: x.strip(), values_with_newline))
    dictionary = {}
    for i in range(len(keys)):
        dictionary.setdefault(keys[i], values[i])
    return dictionary

