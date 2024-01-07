import sys

"""
try: 
    print("Hola,", sys.argv[1])
except IndexError:
    print("Empty Input!")
    """ 

"""
if len(sys.argv) < 2:
    print("Too few argument!")
elif len(sys.argv) > 3:
    print("Too many argument!")
else: 
    print("Hola,", sys.argv[1])
    """

if len(sys.argv) < 2:
    print("Too few argument!")
else:
    for arg in sys.argv[1:]:
        print("Hola,", arg)