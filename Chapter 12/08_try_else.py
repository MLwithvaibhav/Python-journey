try:
    a = int(input("Enter the number you want: "))
    print(a)

except Exception as e:
    print("You are entering a wrong value")
    print(e)

else:
    print("I am inside else")
    
