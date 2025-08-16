try:
    a = int(input("Enter the first number you want: "))
    b = int(input("Enter the second number you want: "))
    print(a/b)

except ZeroDivisionError as v:
    print("Infinite")
    