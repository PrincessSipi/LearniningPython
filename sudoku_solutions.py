L = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]   
for list in L:
    for number in list:
        print(number, end=' ')
# Prints 1 2 3 4 5 6 7 8 9

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

for id, info in D.items():
    print("\nEmployee ID:", id)
    for key in info:
        print(key + ':', info[key])

# Prints Employee ID: emp1
#        name: Bob
#        job: Mgr

#        Employee ID: emp2
#        name: Kim
#        job: Dev

#        Employee ID: emp3
#        name: Sam
#        job: Dev
