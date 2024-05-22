from sys import argv

from ft_filter import ft_filter


def correctArgs() -> bool:
    """Check the arguments"""
    try:
        assert len(argv) == 3, "the arguments are bad"
        try:
            int(argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
    except AssertionError as err:
        print("AssertionError:", err)
        return False
    return True


def filterstring() -> None:
    """filter string"""
    sentence = argv[1].split()
    print(list(ft_filter(lambda word: len(word) > int(argv[2]), sentence)))
    # print([word for word in sentence if len(word) > int(argv[2])])


if __name__ == "__main__":
    if correctArgs():
        filterstring()
