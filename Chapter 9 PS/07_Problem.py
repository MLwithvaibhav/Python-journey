with open ("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present in line. Line no: {lineno}")
        break
    lineno += 1
else:
    print("No python is not present in line")