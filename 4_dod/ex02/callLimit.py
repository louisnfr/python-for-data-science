from typing import Any, Callable


def callLimit(limit: int):
    def decorate(fn: Callable[[], None]):
        count = 0

        def inner(*args: Any, **kwargs: Any):
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {fn} called too many times")
                return
            return fn(*args, **kwargs)

        return inner

    return decorate
