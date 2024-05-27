import matplotlib.pyplot as plt
from load_csv import load


def convert_to_float(number: str) -> float:
    """convert number string to float"""
    if number.endswith("k"):
        return float(number[:-1]) * 1000
    if number.endswith("M"):
        return float(number[:-1]) * 1000000
    return float(number)


def main():
    """main function"""
    data = load("population_total.csv")
    if data.empty:
        return
    france = data[data["country"] == "France"]
    zambia = data[data["country"] == "Zambia"]
    years = data.columns[1:]

    zambiaPop = [convert_to_float(val) for val in zambia.values[0][1:]]
    francePop = [convert_to_float(val) for val in france.values[0][1:]]

    plt.title("Population Projections")
    plt.plot(years, francePop, label="France")
    plt.plot(years, zambiaPop, label="Zambia")
    plt.legend()
    plt.xticks(years[::50])
    maxPop = max(max(francePop), max(zambiaPop))
    yTicks = [i * 1e7 for i in range(int(maxPop / 1e7) + 1)]
    plt.yticks(yTicks, ["{:,.0f}M".format(pop / 1e6) for pop in yTicks])
    plt.show()


if __name__ == "__main__":
    main()
