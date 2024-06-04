from statistics import standard_deviation  # type: ignore

import numpy as np

# arr = [1, 42, 360, 11, 64]
arr = [82, 93, 98, 89, 88]
# arr = [5, 75, 450, 18, 597, 27474, 48575]
# arr = [2, 2, 3, 4, 5, 5, 5, 7, 8, 8, 9, 9, 10, 11, 11, 12]
print(np.std(arr))
print(standard_deviation(arr))

# print(quartile([1, 2, 3]))
# print(quartile([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]))
# print(quartile([10, 2, 38, 23, 38, 23, 21]))

# ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
# print("-----")
# ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
# print("-----")
# ft_statistics(
#     5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem"
# )
# print("-----")
# ft_statistics(toto="mean", tutu="median", tata="quartile")
