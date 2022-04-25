# How to sort a Python dict by value

xs = {'a': 4, 'b': 3, 'c': 3, 'd': 1}

sorted(xs.items(), key=lambda x: x[1])

# or

import operator
sorted(xs.items(), key=operator.itemgetter(1))
