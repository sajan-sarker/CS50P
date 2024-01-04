import sys
try: 
    print("Holla, my name is", sys.argv[1])
except IndexError:
    print("Didn't enter anything")