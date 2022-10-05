result = list(zip(["a", "b", "c"], [1, 2, 3]))  # zip together keys and values
print(result)

d = dict(zip(["a", "b", "c"], [1, 2, 3]))   # make a dict from a zip result
print(d)

d2 = {k: v for (k, v) in zip(["a", "b", "c"], [1, 2, 3])}   # using dictionary comprehension
print(d2)

d3 = {x : x ** 2 for x in [1, 2, 3, 4]}  # or range(1, 5)
print(d3)

d4 = {c : c * 4 for c in "SPAM"}   # loop over any iterable
print(d4)

d5 = {c.lower(): c + "!" for c in ["SPAM", "EGGS", "HAM"]}
print(d5)
