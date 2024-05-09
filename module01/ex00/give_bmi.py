def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    return [weight[i] / height[i] ** 2 for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [val > limit for val in bmi]
