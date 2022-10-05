def anagram(text1,text2):
    text1 = list(text1)
    text2 = list(text2)
    
    for ch in text1:
        if ch not in text2:
            return "Not an anagram!"
    return "Anagram"
    

result= anagram("listen","silent")
print(result)

# correct for lower and uppercase
