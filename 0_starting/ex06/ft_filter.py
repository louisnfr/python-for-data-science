from typing import Callable


def ft_filter(
    function: Callable[[str], bool], iterable: list[str]
) -> list[str]:
    """filter iterables based on a function that returns True or False."""
    return [item for item in iterable if function(item)]
