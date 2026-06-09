#!/usr/bin/env python3
"""Lightweight lint for qiaomu-book-script outputs."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FORBIDDEN_LITERAL = [
    "想象一下",
    "你有没有想过",
    "值得注意的是",
    "不难理解",
    "毋庸置疑",
    "震惊",
    "绝了",
    "太牛了",
    "赋能",
    "落地",
    "深度融合",
    "内卷",
    "这个时代",
    "年轻人",
    "精准打击",
    "重点来了",
    "接下来告诉你",
    "划重点",
    "你知道吗",
    "今天我要告诉你",
    "【停顿】",
    "【加重】",
]

FORBIDDEN_PATTERNS = [
    (re.compile(r"随着[^。！？\n]{0,80}的发展"), "随着……的发展"),
    (re.compile(r"对于[^。！？\n]{0,80}来说"), "对于……来说"),
    (re.compile(r"首先[^。！？\n]{0,240}其次[^。！？\n]{0,240}最后"), "首先……其次……最后"),
    (re.compile(r"^-{3,}$", re.MULTILINE), "水平分隔线 ---"),
    (re.compile(r"^={3,}$", re.MULTILINE), "水平分隔线 ==="),
    (re.compile(r"[—]+"), "破折号"),
]

REQUIRED_LABELS = [
    "第零条：作者介绍与系列引入",
    "第一条：核心观点一",
    "第二条：核心观点二",
    "第三条：核心观点三与系列收尾",
    "第零条",
    "第一条",
    "第二条",
    "第三条",
    "主题一",
    "主题二",
    "主题三",
    "主题四",
    "核心观点一",
    "核心观点二",
    "核心观点三",
    "核心观点四",
]

REQUIRED_OPENING = "大家好，我是向阳乔木"
ALLOWED_CLOSINGS = [
    "感谢你的收看，我是向阳乔木。",
    "感谢你的收看，如果觉得内容有帮助，请一键三连。",
]


def read_text(path: str | None) -> str:
    if not path or path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def fenced_blocks(text: str) -> list[str]:
    return re.findall(r"```(?:[a-zA-Z0-9_-]+)?\n(.*?)```", text, flags=re.DOTALL)


def lint(text: str) -> list[str]:
    errors: list[str] = []
    blocks = fenced_blocks(text)

    if len(blocks) != 1:
        errors.append(f"expected 1 fenced code block, found {len(blocks)}")

    for index, block in enumerate(blocks, start=1):
        stripped = block.strip()
        if not stripped.startswith(REQUIRED_OPENING):
            errors.append(f"script must start with: {REQUIRED_OPENING}")
        if not any(stripped.endswith(closing) for closing in ALLOWED_CLOSINGS):
            endings = " or ".join(ALLOWED_CLOSINGS)
            errors.append(f"script must end with: {endings}")
        if "预估时长" in block:
            errors.append("script contains visible duration metadata")
        for label in REQUIRED_LABELS:
            if label in block:
                errors.append(f"script contains visible internal label: {label}")

    for phrase in FORBIDDEN_LITERAL:
        if phrase in text:
            errors.append(f"forbidden phrase: {phrase}")

    for pattern, label in FORBIDDEN_PATTERNS:
        if pattern.search(text):
            errors.append(f"forbidden pattern: {label}")

    calls_to_action = ["关注", "转发", "分享给", "收藏", "下单", "去买", "购买链接"]
    block_text = blocks[0] if blocks else text
    for phrase in calls_to_action:
        if phrase in block_text:
            errors.append(f"possible extra call to action in final script: {phrase}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint qiaomu-book-script output.")
    parser.add_argument("path", nargs="?", help="Output file path, or stdin when omitted.")
    args = parser.parse_args()

    errors = lint(read_text(args.path))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("qiaomu-book-script lint passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
