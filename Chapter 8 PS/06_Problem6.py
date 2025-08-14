def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter the value in inches: "))
c = inch_to_cms(n)

print(f"The calculated value from inches to cm will be: {c}")
