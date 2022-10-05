text = input("Enter some text ")
midpoint = len(text)//2
left_index = 0
right_index = len(text)-1

while(left_index < right_index):
    if text[left_index] != text[right_index]:
        print("Not a palindrome")
        quit()    # exit()
        
    right_index -= 1
    left_index += 1
print("Is palindrome")    
    
