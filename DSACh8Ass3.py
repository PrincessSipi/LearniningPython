def missing_letter(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    hashtable = {}
    for letter in alphabet:
             if letter  in string:
                 hashtable[letter] = True
             else:
                print(letter)
         
        
sentence= "the quick brown box jumps over the lazy dog"
missing_letter(sentence)
