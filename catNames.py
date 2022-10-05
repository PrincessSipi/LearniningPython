catNames = []
while True:
    name = input ("Enter cat name" + str(len(catNames) + 1) + "(Or Enter nothing to stop):")
    if name == "":
        break
    catNames = catNames + [name] # list concatenation
print("The cat names are:")
for name in catNames:
        print(" " + name)
