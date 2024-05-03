def ft_filter(function, iterable):
    return [x for x in iterable if function(x)]


names = ["John", "Kenny", "Tom", "Bob", "Dilan"]

filtered_names = ft_filter(lambda name: len(name) == 3, names)

print(filtered_names)

for x in filtered_names:
    print(x)
