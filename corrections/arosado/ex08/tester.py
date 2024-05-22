from time import sleep

from Loading import ft_tqdm
from tqdm import tqdm

for elem in ft_tqdm(range(13)):
    sleep(2)
print()
for elem in tqdm(range(13)):
    sleep(2)
print()



7 15 23 30 38 46 52 61 69 76 84 92 100
0 8 15 23 31 38 46 54 62 69 77 85 92 100