import sys

# from sayings import hello
import sayings

if len(sys.argv) == 2:
    sayings.hello(sys.argv[1])
    sayings.goodbye(sys.argv[1])