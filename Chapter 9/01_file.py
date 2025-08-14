from pathlib import Path

# Current script ke folder ka path
file_path = Path(__file__).parent / "file.txt"

with open(file_path) as f:
    content = f.read()

print(content)



f = open("file.txt" "r")
data = f.read()
print(data)
f.close()