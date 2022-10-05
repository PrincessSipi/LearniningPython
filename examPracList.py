lst = [[y for y in range(3)] for x in range(3)]
print(lst)

my_lst = [x*x for x in range(5)]
print(my_lst)


def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(my_lst))

me_lst = [5,6]
for v in range(2):
    print(me_lst[v])
    me_lst.insert(-1, me_lst[v])

print(me_lst)   
