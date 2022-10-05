def missing_letter(string):
    alphabet =dict.fromkeys( ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z'], True)
    #print(string)
   # print(alphabet)
    for letter in string:
        if letter not in alphabet:
            print(letter)

            
missing_letter("the quick brown fox jumps over the lazy dog")
