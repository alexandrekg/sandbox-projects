def simple_generator_fun():
    my_list = [2, 4, 5, 6, 7, 8, 9]
    for i in my_list:
        if i % 2 == 0:
            yield i


for value in simple_generator_fun():
    print(value)

"""
/usr/bin/python3.10 /home/alexkg/workspace/sandbox-projects/books/20-libraries-you-arent-using-but-should/simple-generator-with-yield/main.py 
2
4
6
8
"""
