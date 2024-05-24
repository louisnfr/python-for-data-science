import pandas as pd


def load(path: str) -> pd.DataFrame:
    """load csv"""
    return pd.read_csv(path)
