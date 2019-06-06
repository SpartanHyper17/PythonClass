binum = input("Enter a binary number: ")
binum = str(binum)
length = len(binum)
value = 0
abc = 0
while length > 0:
    last = binum[length - 1]
    if last == "1":
        value = value + 2**abc
    elif last == "0":
        value = value
    else:
        raise Exception("This is not a binary number! Please enter a binary number!")
    abc = abc + 1
    length = length - 1
value = str(value)
print(binum + " is " + value + ".")
