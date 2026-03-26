from src.core import process_batch


def test_process_batch_applies_increment() -> None:
    result = process_batch([1, 2, 3])
    assert result == [3, 5, 7]
