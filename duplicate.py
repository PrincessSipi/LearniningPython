def duplicate(array):
    hashtable = {}
    for element in array:
             if element not in hashtable:
                 hashtable[element] = True
             else:
                print(element)
         
        
array1 = ["a", "b", "c", "d", "c", "e"]
duplicate(array1)
