Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
len('abc')
3
'abc'+'def'
'abcdef'
'Ni!'*5
'Ni!Ni!Ni!Ni!Ni!'
myjob = 'hacker'
for c in myjob: print(c, end='')  #Step through items , print each

hacker
for c in myjob: print(c, end='  ')

h  a  c  k  e  r  
'k' in my job
SyntaxError: invalid syntax
'k' in myjob
True
'K' in myjob
False
'spam' in 'abcspamdef'
True
s = 'spam'
s[0]
's'
s[1], s[-2]
('p', 'a')
s[1:3], s[1:], s[:-1]
('pa', 'pam', 'spa')
s ='abcdefghikjlmnop'
s[1:10:2]
'bdfhk'
s[::2]
'acegijmo'
s='hello'
s[::-1]
'olleh'
s='abcedfg'
s[5:1:-1]
'fdec'
'spam'[1:3]
'pa'
'spam'[slice(1,3)]
'pa'
'spam'[::-1]
'maps'
'spam'[slice(None, None, -1)]
'maps'
