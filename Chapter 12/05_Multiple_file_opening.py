with open('file1.txt') as f1, open('file2.txt') as f2:
    # Process files
    data1 = f1.read()
    data2 = f2.read()
    print(data1, data2)
