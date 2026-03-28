from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulate deployment to staging")
    parser.add_argument("--artifact", default="artifact/build.txt", help="Path to build artifact")
    parser.add_argument(
        "--output",
        default="staging/staging-deploy.txt",
        help="Path to save staging deployment report",
    )
    args = parser.parse_args()

    artifact_path = Path(args.artifact)
    if not artifact_path.exists():
        raise FileNotFoundError(f"Artifact not found: {artifact_path}")

    artifact_content = artifact_path.read_text(encoding="utf-8")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "environment=staging\n" + artifact_content,
        encoding="utf-8",
    )

    print("Staging deploy simulation complete")
    print(output_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
