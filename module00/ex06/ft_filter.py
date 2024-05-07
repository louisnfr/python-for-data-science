def ft_filter(function, iterable):
    """filter iterables based on a function that returns True or False."""
    if function:
        return (item for item in iterable if function(item))
    else:
        return (item for item in iterable if item)


filtered = filter(None, ["1", True, 12, 0, None, False])


for x in filtered:
    print(x)
