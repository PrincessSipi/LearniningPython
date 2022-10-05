word1 = list(input("First word "))
word2 = list(input("Second word "))
for ch in word1:
    if ch not in word2:
        print("Not an anagram")
        exit()
print("Anagram found")
