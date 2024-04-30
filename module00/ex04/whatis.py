import sys

if len(sys.argv) > 2:
  print("AssertionError: more than one argument is provided")
  exit()
elif len(sys.argv) == 1:
  exit()

try:
    int(sys.argv[1])
except:
    print("AssertionError: argument is not an integer")
    exit()

if int(sys.argv[1]) % 2:
    print("I'm Odd.")
else:
    print("I'm Even.")
