import os
from typing import Any, Generator


def ft_tqdm(lst: range) -> Generator[Any, Any, Any]:
    """Print a progress bar"""
    size_of_terminal = os.get_terminal_size().columns - 40

    for i, _ in enumerate(lst, 1):
        bar_formula = i * size_of_terminal // len(lst)
        percentage = (i * 100) // len(lst)
        progress_bar = f"{'█' * bar_formula:<{size_of_terminal}}"
        print(f"\r{percentage:>3}%|{progress_bar}| {i}/{len(lst)}", end="")
        yield i
