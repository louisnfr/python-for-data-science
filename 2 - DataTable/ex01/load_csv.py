import pandas as pd


def load(path: str) -> pd.DataFrame:
    """load csv"""
    try:
        return pd.read_csv(path)
    except Exception as e:
        print("Error:", e)
        return pd.DataFrame(None)
