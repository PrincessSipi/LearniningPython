def print_msg(msg):
    # this is the outer enclosing function
    def printer():
        # This is the nested function
        print(msg)
    return printer


# we execute the function
#Output "Hello"
print_msg("Hello")
another = print_msg("Hello")
another()
 
