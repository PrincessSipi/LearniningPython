Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 1234
res = ' integers : ...%d...%-6d...%06d' %(x, x, x)
res
' integers : ...1234...1234  ...001234'
res = ' integers : ...%d...%6d...%06d' %(x, x, x)
res
' integers : ...1234...  1234...001234'
x = 1.23456789
x
1.23456789
'%e | %f | %g' %(x, x, x)
'1.234568e+00 | 1.234568 | 1.23457'
'%E'%x
'1.234568E+00'
'%-6.2f |%05.2f | %+06.1f' %(x, x, x)
'1.23   |01.23 | +001.2'
'%-6.2f |%05.3f | %06.1f' %(x, x, x)
'1.23   |1.235 | 0001.2'
