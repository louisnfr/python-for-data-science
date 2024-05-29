import matplotlib.pyplot as plt
from load_csv import load


def main():
    """main function"""
    data = load("life_expectancy_years.csv")
    if data.empty:
        return
    france = data[data["country"] == "France"]
    years = france.columns[1:]

    plt.plot(years, france.values[0][1:], label="France")
    plt.xticks(years[::50])
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
