def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """gives the BMI of a person based on their height and weight."""
    bmis: list[float] = []
    try:
        for i in range(len(height)):
            bmis.append(weight[i] / height[i] ** 2)
    except Exception as e:
        print("Error:", e)
        return []
    return bmis


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    takes a list of BMI values and a limit, and returns a list of booleans
    indicating whether each BMI value is above the limit.
    """
    return [val > limit for val in bmi]
