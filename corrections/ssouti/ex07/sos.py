from sys import argv


def encode_to_morse(message: str) -> str:
    """encode a message to morse code"""
    morse_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        " ": "/",
    }
    encoded = []
    for c in message.upper():
        if c not in morse_dict:
            raise AssertionError(f"Bad argument: {c} is not a valid character")
        encoded.append(morse_dict[c])
    print(" ".join(encoded))


def main():
    """main function"""
    if len(argv) != 2:
        print("Usage: python sos.py <message>")
        return
    try:
        encode_to_morse(argv[1])
    except AssertionError as err:
        print(err)


if __name__ == "__main__":
    main()
