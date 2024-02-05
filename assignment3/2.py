inches = 2.54
i = float(input("Enter inches to convert them into centimetres: "))
while i >= 0:
    res = inches*i
    print(res)
    i = float(input("Enter another value of inches or enter negetive number to end this program"))
else:
    print("End program")