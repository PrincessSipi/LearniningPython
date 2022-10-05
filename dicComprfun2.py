d = dict.fromkeys(["a", "b", "c", ], True)   # initialize dictionary from keys
print(d)
d1 = {k: 0 for k in ["a", "b", "c"]}  # same as above but with dictionary comprehension
print(d1)
s = dict.fromkeys("spam")
print(s)
s1 = {k: None for k in "spam"}
print(s1)
