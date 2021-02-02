import mymodule

while True:
    print("Enter a number to check prime.(If you want to exit program then enter 'x')")
    num = input("Enter: ")
    if num == 'x':
        break
    else:
        result = mymodule.primecheck(int(num))
        print(result)
