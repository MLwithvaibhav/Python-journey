f = open("Poem.txt")
content = f.read()

if ("Twinkle" in content):
    print("The word present in content")

else:
    print("The word is not present in content")