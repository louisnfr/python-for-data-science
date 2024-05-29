import sys

if len(sys.argv) > 1:
    try:
        if len(sys.argv) != 2:
            raise AssertionError("more than one argument is provided")
        try:
            i = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        if i % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as err:
        print("AssertionError:", err)
