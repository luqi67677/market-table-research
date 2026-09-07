#!/usr/bin/env python3
"""Build a WorkBuddy-compatible zip without changing the canonical SKILL.md."""

from __future__ import annotations

import argparse
import shutil
import tempfile
import zipfile
from pathlib import Path


SKILL_NAME = "market-table-research"
WORKBUDDY_FIELDS = """display_name: 市场分析与竞品调研
display_name_en: Market Table Research
description_zh: 基于公开证据开展市场、竞品、用户与产品调研，输出来源可追溯的决策报告。
description_en: Evidence-driven market, competitor, user, and product research with traceable decision-ready reports.
version: 1.5.0
author: luqi67677
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="生成 WorkBuddy 兼容的 Skill ZIP")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("dist") / f"{SKILL_NAME}-workbuddy.zip",
        help="输出 ZIP，默认 dist/market-table-research-workbuddy.zip",
    )
    return parser.parse_args()


def add_workbuddy_frontmatter(skill_text: str) -> str:
    if not skill_text.startswith("---\n"):
        raise ValueError("SKILL.md 缺少 YAML frontmatter")

    closing = skill_text.find("\n---\n", 4)
    if closing == -1:
        raise ValueError("SKILL.md 的 YAML frontmatter 未闭合")

    frontmatter = skill_text[4:closing].rstrip()
    body = skill_text[closing + 5 :].replace(
        "[README](README.md)",
        "[README](https://github.com/luqi67677/market-table-research/blob/main/README.md)",
    )
    return f"---\n{frontmatter}\n{WORKBUDDY_FIELDS}---\n{body}"


def write_zip(source_root: Path, output: Path) -> None:
    skill_path = source_root / "SKILL.md"
    if not skill_path.is_file():
        raise FileNotFoundError(f"缺少 {skill_path}")

    output = output.expanduser()
    if not output.is_absolute():
        output = source_root / output
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="market-table-research-workbuddy-") as tmp:
        package_skill = Path(tmp) / "skills" / SKILL_NAME
        package_skill.mkdir(parents=True)
        package_skill.joinpath("SKILL.md").write_text(
            add_workbuddy_frontmatter(skill_path.read_text(encoding="utf-8")),
            encoding="utf-8",
        )

        for folder_name in ("references", "assets"):
            source = source_root / folder_name
            if source.is_dir():
                shutil.copytree(source, package_skill / folder_name)

        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(Path(tmp).rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(tmp))

    print(f"PASS: {output}")


def main() -> int:
    args = parse_args()
    source_root = Path(__file__).resolve().parents[1]
    try:
        write_zip(source_root, args.output)
    except (FileNotFoundError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
