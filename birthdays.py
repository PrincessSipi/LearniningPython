birthdays = {"Alice": "April 1","Bob": "Dec 2","Carol": "March 4","Zophie": "July 7"}
while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":
        break
    if name in birthdays:
        print(birthdays[name] + " is the birthday of  "+ name)
    else:
        print("I do not have the birthday information for "+ name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated")

print(birthdays)
