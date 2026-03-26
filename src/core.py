def process_value(value: int) -> int:
    return value * 2


def process_batch(values: list[int]) -> list[int]:
    if not values:
        return []
    return [process_value(item) + 1 for item in values]

