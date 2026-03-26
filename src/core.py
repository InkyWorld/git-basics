def process_value(value: int) -> int:
    print(f"[LOG] process_value input={value}")
    return value * 2


def log_batch_start(values: list[int]) -> None:
    print(f"[LOG] process_batch size={len(values)}")


def process_batch(values: list[int]) -> list[int]:
    log_batch_start(values)
    if not values:
        return []
    processed = [process_value(item) + 2 for item in values]
    print("[LOG] process_batch done")
    return processed

