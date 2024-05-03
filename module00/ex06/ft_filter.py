def ft_filter(function_to_apply, list_of_inputs: list):
    return [x for x in list_of_inputs if function_to_apply(x)]


names = ["John", "Kenny", "Tom", "Bob", "Dilan"]

filtered_names = ft_filter(lambda name: len(name) == 3, names)

print(filtered_names)

for x in filtered_names:
    print(x)
