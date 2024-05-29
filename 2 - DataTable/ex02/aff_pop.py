import matplotlib.pyplot as plt
from load_csv import load


def y_formatter(x: float, pos: float) -> str:
    """format y-axis"""
    if x >= 1_000_000:
        return f"{x/1_000_000:.0f}M"
    return f"{x/1_000}k"


def convert_to_float(number: str) -> float:
    """convert number string to float"""
    if number.endswith("k"):
        return float(number[:-1]) * 1_000
    if number.endswith("M"):
        return float(number[:-1]) * 1_000_000
    return float(number)


def main():
    """main function"""
    data = load("population_total.csv")
    if data.empty:
        return

    france = data[data["country"] == "France"]
    zambia = data[data["country"] == "Zambia"]
    years = data.columns[1:-50]

    zambiaPop = [convert_to_float(val) for val in zambia.values[0][1:-50]]
    francePop = [convert_to_float(val) for val in france.values[0][1:-50]]

    plt.plot(years, francePop, label="France")
    plt.plot(years, zambiaPop, label="Zambia")

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc="lower right")

    plt.xticks(years[::50])
    plt.yticks([20_000_000, 40_000_000, 60_000_000])
    plt.gca().yaxis.set_major_formatter(y_formatter)

    plt.show()


if __name__ == "__main__":
    main()
