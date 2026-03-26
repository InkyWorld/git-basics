def is_positive(value: int) -> bool:
    return value > 0


def validate_non_empty(raw: str) -> bool:
    return raw.strip() != ""


def validate_all_positive(values: list[int]) -> bool:
    for value in values:
        if not is_positive(value):
            return False
    return True

