def parse_int(raw: str) -> int:
    return int(raw.strip())


def parse_int_list(raw: str) -> list[int]:
    items = raw.split(",")
    result: list[int] = []
    for item in items:
        result.append(parse_int(item))
    return result

