a = int(input("Enter the first number you want: "))
b = int(input("Enter the second number you want: "))

if (b==0):
    raise ZeroDivisionError("the number you are trying to enter is forbidden")
    print("Thank you")

else:
    print(f"The division of both the numbers will be: {a/b}")