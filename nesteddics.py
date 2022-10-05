rec = {}
rec["name"] = "Bob"
rec["age"] = 40.5
rec["job"] = "developer/ manager"

print(rec["name"])
print(rec)

rec2 = {"name": "Bob",
        "jobs": ["developer", "manager"],
        "web": "www.bobs.org/Bob",
        "home": {"state": "Overworked", "zip": "12345"}}
print(rec2["jobs"])
print(rec2["jobs"][1])
print(rec2["home"]["zip"])
print(rec2)
database1 ={"rec1": {"name": "Bob",
        "jobs": ["developer", "manager"],
        "web": "www.bobs.org/Bob",
        "home": {"state": "Overworked", "zip": "12345"}},
          "rec2":{"name": "Sam",
        "jobs": ["tutor", "dad"],
        "web": "www.sams.org/Sam",
        "home": {"state": "Shilton", "zip": "12356"}}}
print(database1["rec2"])

# ways to create a dictionary
{"name": "Bob", "age": 40}   # traditional literal expression
D = {}  # assign by keys dynamically
D["name"] = "Bob"  
D["age"] = 40
dict(name = "Bob", age = 40)  # dict keyword argument form
dict[("name", "Bob"), ("age", 40)]  # dict key/value form
dict.fromkeys(["a", "b"], 0)
print(dict)

