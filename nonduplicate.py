#def nonduplicate(string):
   # hashtable = {}
   # dups = []
    #for element in string:
         #    if element not in hashtable:
           #      hashtable[element] = True
             #    if element in hashtable:
               #      hashtable[element]+= 1
                 #else:
                   #  hashtable[element] = 1
                     #dups.append(element)
                     
  #  for element in dups:
    #    if hashtable[element] == 1:
      #      print(dups)
    #return None
         
        
s = "minimum"
#print(nonduplicate(s))
t =[a for a in s if s.count(a) == 1]
print(t)
