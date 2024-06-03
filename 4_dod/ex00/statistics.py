def median(args: list[int]) -> float:
    sort = sorted(args)
    middle = len(sort) // 2
    if len(sort) % 2 == 0:
        return mean([sort[middle], sort[middle - 1]])
    else:
        return sort[middle]


def mean(args: list[int]) -> float:
    return sum(args) / len(args)


def ft_statistics(*args: int, **kwargs: str) -> None:
    array = list(args)
    # for arg in args:
    #     print(arg)
    # for key, value in kwargs.items():
    #     print(f"{key}={value}")
