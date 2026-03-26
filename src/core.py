def process_value(value: int) -> int:
    print(f"[LOG] process_value input={value}")
    return value * 2


def process_batch(values: list[int]) -> list[int]:
    if not values:
        return []
    return [process_value(item) + 1 for item in values]

