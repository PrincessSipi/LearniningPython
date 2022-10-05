Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = "spammy"
s = [:3] + "xx"+ s[5:]
SyntaxError: invalid syntax
s[:3]
'spa'
s = s[:3] + 'xx' + s[5:]
s
'spaxxy'
s = s.replace('xx', 'mm')
s
'spammy'
'aa$bb$cc$dd'.replace('$','SPAM')
'aaSPAMbbSPAMccSPAMdd'
s = 'xxxxSPAMxxxxSPAMxxxx'
where = s.find('SPAM')
where
4
s = s[:where] +'EGGS' + s[(where + 4)]
s
'xxxxEGGSx'
s.replace('SPAM', 'EGGS')
'xxxxEGGSx'
s = 'xxxxSPAMxxxxSPAMxxxx'
S
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    S
NameError: name 'S' is not defined. Did you mean: 's'?
s
'xxxxSPAMxxxxSPAMxxxx'
s.replace('SPAM', 'EGGS')
'xxxxEGGSxxxxEGGSxxxx'
s = 'xxxxSPAMxxxxSPAMxxxx'
s.replace('SPAM', 'EGGS', 1)
'xxxxEGGSxxxxSPAMxxxx'
