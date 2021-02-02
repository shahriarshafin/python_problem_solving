def primecheck(num):
    if -1 < num < 20:
        file = open("priems.txt", "rt")
        line = file.readlines()
        prime_number_list = list(map(lambda x: x.strip(), line))
        if str(num) in prime_number_list:
            return "prime"
        else:
            return "Not prime"
        file.close()
    else:
        return "Out of Range"


