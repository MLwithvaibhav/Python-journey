def greatest(a, b, c):
    if (a>b and a>c):
        return(a)
    if (b>a and b>c):
        return(a)
    if (c>b and c>a):
        return(a)
    
a = 23
b = 3
c = 2

print(greatest(a, b, c))