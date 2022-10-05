def palindrome(text):
    text= list(text)
    start_index = 0
    last_index = len(text)-1
    for ch in text:    
        if text[start_index] != text[last_index]:
            return "Not palindrome"
            exit()
    return "palindrome"
    
    
result = palindrome("ten animals I slam in a net")
print(result)
