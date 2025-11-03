try:
    # value = 10/0
    # print(value)
    userinput = int(input('Enter number \n'))
    print(userinput+5)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
