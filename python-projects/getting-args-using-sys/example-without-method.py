import sys

all_args = sys.argv
print(all_args)

name_of_script = sys.argv[0]
print('Script name :' + name_of_script)

first_arg = sys.argv[1]
print('My first name :' + first_arg)

second_arg = sys.argv[2]
print('My last name :' + second_arg)

"""
[master][~/workspace/sandbox-projects/python-projects/getting-args-using-sys]$ python example-without-method.py Alexandre Giacobo                        
['example-without-method.py', 'Alexandre', 'Giacobo']
Script name :example-without-method.py
My first name :Alexandre
My last name :Giacobo
"""