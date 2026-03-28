from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a build artifact for CI/CD pipeline")
    parser.add_argument("--output", default="artifact/build.txt", help="Artifact output path")
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    build_id = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    content = f"build_id={build_id}\nstatus=ready\n"
    output_path.write_text(content, encoding="utf-8")

    print(f"Build artifact created: {output_path}")
    print(content)


if __name__ == "__main__":
    main()
