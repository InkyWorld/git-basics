def process_value(value: int) -> int:
    return value * 2


def process_batch(values: list[int]) -> list[int]:
    return [process_value(item) for item in values]

