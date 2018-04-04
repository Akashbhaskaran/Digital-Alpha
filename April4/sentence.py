import re

str = "#Python is an interpreted high level programming language for general-purpose programming*."
str = re.sub('[^A-Za-z0-9]+', ' ', str)

print("After removing special characters")
print (str)

print("Repeated word counts")
words = str.split()
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1
print(counts)

print("Pallindrome Words")
for word in words:
    if word == word[::-1] :
        print (word)
