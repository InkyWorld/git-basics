def process_value(value: int) -> int:
    return value * 2


def process_batch(values: list[int]) -> list[int]:
    result: list[int] = []
    for item in values:
        result.append(process_value(item))
    return result

