def mean(data: list[int]) -> float:
    """returns mean of list"""
    m = sum(data) / len(data)
    return m


def median(data: list[int]) -> float:
    """returns median of list"""
    sort = sorted(data)
    middle = len(sort) // 2
    if len(sort) % 2 == 0:
        return mean([sort[middle], sort[middle - 1]])
    else:
        return sort[middle]


def percentile(data: list[int], percentile: int) -> float:
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


def print_percentiles(data: list[int]) -> list[float]:
    """prints percentiles 25 and 75"""
    return [percentile(data, 25), percentile(data, 75)]


def std(data: list[int]) -> float:
    """returns standard deviation"""
    m = mean(data)
    s = sum([(x - m) ** 2 for x in data])
    return (s / len(data)) ** 0.5


def var(data: list[int]) -> float:
    """returns variance"""
    m = mean(data)
    s = sum([(x - m) ** 2 for x in data])
    return s / len(data)


def ft_statistics(*args: int, **kwargs: str) -> None:
    """main function"""
    data = list(args)
    options = {
        "mean": mean,
        "median": median,
        "quartile": print_percentiles,
        "std": std,
        "var": var,
    }
    for value in kwargs.values():
        if len(data) == 0:
            print("ERROR")
            continue
        if value in options:
            print(f"{value} : {options[value](data)}")
