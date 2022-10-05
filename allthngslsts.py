Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = ["Alice", "Bob", "ants", "badgers", "cats", "Carol"]
spam.sort()
spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
spam.sort(key = str.lower)
spam
['Alice', 'ants', 'badgers', 'Bob', 'Carol', 'cats']
spam.reverse
<built-in method reverse of list object at 0x00000255FBEAC400>
spam.reverse()
spam
['cats', 'Carol', 'Bob', 'badgers', 'ants', 'Alice']
name = "Siphiwe"
name_list = list(name)
name_list
['S', 'i', 'p', 'h', 'i', 'w', 'e']
eggs = ("hello", 42, 0.5)
eggs[0]
'hello'
eggs[:1]
('hello',)
eggs[:2]
('hello', 42)
eggs[1:2]
(42,)
del eggs[2]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    del eggs[2]
TypeError: 'tuple' object doesn't support item deletion
eggs.append(2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    eggs.append(2)
AttributeError: 'tuple' object has no attribute 'append'
len(eggs)
3
import copy
spam = ["A", "B", "C", "D"]
id(spam)
2568322024512
cheese = copy.copy(spam)
id(cheese)
2568322085696
cheese[1] = 42
spam
['A', 'B', 'C', 'D']
cheese
['A', 42, 'C', 'D']
