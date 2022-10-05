foo = (1, 2, 3)
print(foo.index(3))

dct = {}
dct["1"] = (1,2)
dct["2"] = (2,1)

for x in dct.keys():
    print(dct[x][1], end="")

my_list = [1, 2]
for v in range(2):
    my_list.insert(-1, my_list[v])
print(my_list)

print(1//2)