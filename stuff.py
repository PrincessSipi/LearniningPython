Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2**100
1267650600228229401496703205376
len(str(2 ** 1000000)) # How many digits in a really big number
301030
4*3
12
5+1
6
3.1415*2
6.283
import math
math.pi
3.141592653589793
math.sqrt
<built-in function sqrt>
math.sqrt(85)
9.219544457292887
import randon
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    import randon
ModuleNotFoundError: No module named 'randon'
import random
randon.randint(1,5)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    randon.randint(1,5)
NameError: name 'randon' is not defined. Did you mean: 'random'?
random.randint(2,9)
6

random.random()
0.12364921452042121
random.choice(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    random.choice(1,2,3,4,5)
TypeError: Random.choice() takes 2 positional arguments but 6 were given
random.choice([1, 2, 3, 4, 5])
5
random.choice([1, 2, 3, 4, 5])
4
S = "When?"
len(S)
5
S[3]
'n'
S[:3]
'Whe'
S[3:]
'n?'
S[-1]
'?'
S + "are"
'When?are'
S**4
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    S**4
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
S * 8
'When?When?When?When?When?When?When?When?'
del(S[0])
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    del(S[0])
TypeError: 'str' object doesn't support item deletion
s = "shrubbery"
l = list(s)
l
['s', 'h', 'r', 'u', 'b', 'b', 'e', 'r', 'y']
l[1] = "c"
l
['s', 'c', 'r', 'u', 'b', 'b', 'e', 'r', 'y']
"".join(l)
'scrubbery'
