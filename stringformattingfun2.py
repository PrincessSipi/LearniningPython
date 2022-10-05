Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
template = '{0}, {1},  and {2}'
template.format('egg', 'beans', 'bacon')
'egg, beans,  and bacon'
template = '{motto}, {pork},  and {food}'
template.format(motto ='egg', food='beans',pork = 'bacon')
'egg, bacon,  and beans'
template = '{motto}, {0},  and {food}'
template.format(motto ='egg', food='beans', 'bacon')
SyntaxError: positional argument follows keyword argument
template.format(motto ='egg', 'bacon', food='beans'')
                
SyntaxError: unterminated string literal (detected at line 1)
template.format(motto ='egg', 'bacon', food='beans')
                
SyntaxError: positional argument follows keyword argument
template = '{motto}, {0},  and {food}'
                
template.format(motto ='egg', 'bacon', food='beans')
                
SyntaxError: positional argument follows keyword argument
template = '{motto}, {1},  and {food}'
                
template.format(motto ='egg', 'bacon', food='beans')
                
SyntaxError: positional argument follows keyword argument
template = '{motto}, {0},  and {food}'
                
template.format('bacon', motto ='egg', food='beans')
                
'egg, bacon,  and beans'
template = '{}, {},  and {}'
                
template.format('egg', 'beans', 'bacon')
                
'egg, beans,  and bacon'
