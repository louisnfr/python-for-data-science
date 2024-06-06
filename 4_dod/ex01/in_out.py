from typing import Callable

MathFunc = Callable[[int | float], int | float]
InnerFunc = Callable[[], int | float]


def square(x: int | float) -> int | float:
    return x * x


def pow(x: int | float) -> int | float:
    return x**x


def outer(x: int | float, function: MathFunc) -> InnerFunc:
    count = 0

    def inner() -> int | float:
        nonlocal count
        count += 1
        result = x
        for _ in range(count):
            result = function(result)
        return result

    return inner
