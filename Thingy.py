n = input("Enter a number: ")
n = int(n)
if n > 1000:
    print("PLEASE ENTER A NUMBER THAT IS LESS THAN 1000!")
else:
    n = str(n)
    if len(n) == 2:
        if n[0] == "2":
            a = "Twenty"
        if n[0] == "3":
            a = "Thirty"
        if n[0] == "4":
            a = "Fourty"
        if n[0] == "5":
            a = "Fifty"
        if n[0] == "6":
            a = "Sixty"
        if n[0] == "7":
            a = "Seventy"
        if n[0] == "8":
            a = "Eighty"
        if n[0] == "9":
            a = "Ninety"
        if n[1] == "0":
            b = ""
        if n[1] == "1":
            b = "-One"
        if n[1] == "2":
            b = "-Two"
        if n[1] == "3":
            b = "-Three"
        if n[1] == "4":
            b = "-Four"
        if n[1] == "5":
            b = "-Five"
        if n[1] == "6":
            b = "-Six"
        if n[1] == "7":
            b = "-Seven"
        if n[1] == "8":
            b = "-Eight"
        if n[1] == "9":
            b = "-Nine"
    print(a + b)
