import os

path = '/'  # Is directory ko specify kar raha hai
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

print("Files in current directory:")
for file in files:
    print(file)
