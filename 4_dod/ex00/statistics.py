def median(args: list[int]) -> float:
    """returns median of list"""
    print(f"median of {args}")
    sort = sorted(args)
    middle = len(sort) // 2
    if len(sort) % 2 == 0:
        return mean([sort[middle], sort[middle - 1]])
    else:
        return sort[middle]


def mean(args: list[int]) -> float:
    """returns mean of list"""
    return sum(args) / len(args)


def quartile(args: list[int]):
    """returns q1 and q3 of list"""
    sort = sorted(args)
    middle = len(sort) // 2

    q1 = median(sort[:middle])
    q3 = median(sort[-middle:])
    print(f"Q1 {q1}\nQ3 {q3}")
    return [q1, q3]
    print(f"q1: {q1}\nq3: {q3}")


def ft_statistics(*args: int, **kwargs: str) -> None:
    """main function"""
    # array = list(args)
    # for arg in args:
    #     print(arg)
    # for key, value in kwargs.items():
    #     print(f"{key}={value}")
    pass
