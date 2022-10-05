Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = 'spammy'
l = list(s)
l
['s', 'p', 'a', 'm', 'm', 'y']
l[3]= 'x'
l
['s', 'p', 'a', 'x', 'm', 'y']
l[4] = 'x'
l
['s', 'p', 'a', 'x', 'x', 'y']
s = ''.join(l)
s
'spaxxy'
'SPAM'.join(['eggs', 'sausage', 'ham', 'toast'])
'eggsSPAMsausageSPAMhamSPAMtoast'
'*****'.join(['eggs', 'sausage', 'ham', 'toast'])
'eggs*****sausage*****ham*****toast'
'       '.join(['eggs', 'sausage', 'ham', 'toast'])
'eggs       sausage       ham       toast'
line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
col1
'aaa'
col3
'ccc'
cols = line.split()
cols
['aaa', 'bbb', 'ccc']
d= 'dummy'
d.split()
['dummy']
t = d.split()
t
['dummy']
line = 'bob,hacker,40'
line.split(',')
['bob', 'hacker', '40']
line = "I'mSPAMaSPAMlumberjack"
line.split("SPAM")
["I'm", 'a', 'lumberjack']
line = "the knights who say Ni\n"
line.rstrip()
'the knights who say Ni'
line.upper()
'THE KNIGHTS WHO SAY NI\n'
line.isalpha()
False
line.endswith('Ni\n')
True
line.startswith('The')
False
line.startswith('the')
True
line
'the knights who say Ni\n'
line.find('Ni') != -1
True
'Ni' in line
True
sub = 'Ni\n'
line.endswith(sub)
True
line[-len(sub):] == sub
True
