Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'%(qty)d more %(food)s' %{'qty': 1 , 'food':' egg'}
'1 more  egg'
reply = """Greetings..."""
reply = """Greetings...
Hello %(name)s!
Your age is %(age)s
"""
values = {'name':'Sipi', 'age':40}
print(reply%values)
Greetings...
Hello Sipi!
Your age is 40

