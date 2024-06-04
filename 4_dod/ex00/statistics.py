def ft_mean(data: list[int]) -> float:
    """returns mean of list"""
    return sum(data) / len(data)


def ft_median(data: list[int]) -> float:
    """returns median of list"""
    print(f"median of {data}")
    sort = sorted(data)
    middle = len(sort) // 2
    if len(sort) % 2 == 0:
        return ft_mean([sort[middle], sort[middle - 1]])
    else:
        return sort[middle]


def ft_percentile(data: list[int], percentile: int) -> float:
    """returns percentile value"""
    data = sorted(data)

    index = (len(data) - 1) * percentile / 100

    lower_index = int(index)
    upper_index = lower_index + 1

    lower_value = data[lower_index]
    upper_value = data[upper_index]
    fraction = index - lower_index

    ret = lower_value + (upper_value - lower_value) * fraction
    return ret


def ft_std(data: list[int]) -> float:
    """returns standard deviation"""
    m = ft_mean(data)
    s = sum([(x - m) ** 2 for x in data])
    return (s / len(data)) ** 0.5


def ft_var(data: list[int]) -> float:
    """returns variance"""
    return 0


def ft_statistics(*args: int, **kwargs: str) -> None:
    """main function"""
    # array = list(args)
    # for arg in args:
    #     print(arg)
    # for key, value in kwargs.items():
    #     print(f"{key}={value}")
    pass
