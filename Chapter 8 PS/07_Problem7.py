# Question:
# Write a function that takes a list of strings and a word, 
# and returns a new list with the given word removed from the list. 
# Additionally, remove any matching characters from the start or end of the remaining strings.

# Approach:
# 1. Create an empty list to store the modified strings.
# 2. Loop through each item in the given list.
# 3. If the current item is not exactly equal to the word:
#    a) Use strip(word) to remove any characters from 'word' 
#       that appear at the start or end of the item.
#    b) Append the modified item to the result list.
# 4. Return the result list.

def rem(l, word):
    n = []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n


# Dry Run:
# Input:
# l = ["Harry", "Rohan", "Shubham", "an"]
# word = "an"
#
# Step 1: item = "Harry"
#   "Harry" != "an" → True
#   "Harry".strip("an") → "Harry"  (no change)
#   n = ["Harry"]
#
# Step 2: item = "Rohan"
#   "Rohan" != "an" → True
#   "Rohan".strip("an") → "Roha" (removed 'n' from end)
#   n = ["Harry", "Roha"]
#
# Step 3: item = "Shubham"
#   "Shubham" != "an" → True
#   "Shubham".strip("an") → "Shubham" (no change)
#   n = ["Harry", "Roha", "Shubham"]
#
# Step 4: item = "an"
#   "an" != "an" → False → skip
#
# Final Output:
# ["Harry", "Roha", "Shubham"]

l = ["Harry", "Rohan", "Shubham", "an"]
print(rem(l, "an"))
