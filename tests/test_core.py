import unittest
import importlib.util
from pathlib import Path

CORE_PATH = Path(__file__).resolve().parents[1] / "src" / "core.py"
SPEC = importlib.util.spec_from_file_location("core_module", CORE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Failed to load src/core.py")

CORE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)


class CoreTests(unittest.TestCase):
    def test_process_value_doubles_number(self) -> None:
        self.assertEqual(CORE.process_value(3), 6)

    def test_process_batch_transforms_list(self) -> None:
        # process_value(x) * 2 and process_batch adds +1 to each item
        self.assertEqual(CORE.process_batch([1, 2, 3]), [3, 5, 7])


if __name__ == "__main__":
    unittest.main()
