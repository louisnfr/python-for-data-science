from typing import Any

import matplotlib.pyplot as plt
from load_csv import load
from pandas import Series


def main():
    """main function"""
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy = load("life_expectancy_years.csv")
    if income.empty or life_expectancy.empty:
        return

    income_1900: Series[Any] = income["1900"]
    life_expectancy_1900: Series[Any] = life_expectancy["1900"]

    plt.scatter(income_1900, life_expectancy_1900)

    plt.title("1900")
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")

    plt.xscale("log")
    plt.xticks([300, 1_000, 10_000], labels=["300", "1k", "10k"])

    plt.show()


if __name__ == "__main__":
    main()
