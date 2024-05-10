import sys


def countChars(string: str):
    """Count the number of characters in a string."""
    charset = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    uppercase = sum(1 for c in string if c.isupper())
    lowercase = sum(1 for c in string if c.islower())
    punctuation = sum(1 for c in string if c in charset)
    spaces = sum(1 for c in string if c.isspace())
    digits = sum(1 for c in string if c.isdigit())
    print(f"The text contains {len(string)} characters:")
    print(f"{uppercase} upper letters")
    print(f"{lowercase} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """main function"""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
    except AssertionError as err:
        print("AssertionError:", err)
        exit()

    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
        countChars(text)
    else:
        countChars(sys.argv[1])


if __name__ == "__main__":
    main()
