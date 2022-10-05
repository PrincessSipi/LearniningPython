word1 = input("First word ")
word2 = input("Second word ")
for ch in word2:
    if ch not in word1:
        print("Not found")
        exit()
#print(word1.find(word2))
print("Found")
