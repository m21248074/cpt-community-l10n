#!/usr/bin/env python3
"""把已翻譯的字串套用到「原文完全相同」但尚未翻譯的項目。

只在同一原文的所有既有譯文一致時才套用；有分歧的原文會列出供人工處理。
套用後的項目移除 type="unfinished"。

用法：python tools/apply_duplicates.py [--dry-run] [檔案]
"""
import argparse
import collections
import re
import sys

DEFAULT = "zh-TW/Chinese Traditional.ts"
CJK = re.compile("[一-鿿]")
MSG = re.compile(r"<message\b[^>]*>.*?</message>", re.S)
SRC = re.compile(r"<source>(.*?)</source>", re.S)
TR = re.compile(r"<translation([^>]*)>(.*?)</translation>", re.S)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?", default=DEFAULT)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    text = open(args.file, encoding="utf-8", newline="").read()

    known = collections.defaultdict(collections.Counter)
    for m in MSG.finditer(text):
        s, t = SRC.search(m.group(0)), TR.search(m.group(0))
        if s and t and "numerus" not in m.group(0)[:60] and CJK.search(t.group(2)):
            known[s.group(1)][t.group(2)] += 1

    conflicts = {s: c for s, c in known.items() if len(c) > 1}
    applied = 0

    def repl(m):
        nonlocal applied
        block = m.group(0)
        s, t = SRC.search(block), TR.search(block)
        if not (s and t) or "numerus=" in block.split(">", 1)[0]:
            return block
        if CJK.search(t.group(2)) or s.group(1) not in known or s.group(1) in conflicts:
            return block
        new = next(iter(known[s.group(1)]))
        applied += 1
        return block[: t.start()] + "<translation>" + new + "</translation>" + block[t.end():]

    out = MSG.sub(repl, text)
    print(f"套用 {applied} 筆；譯文分歧的原文 {len(conflicts)} 個（未處理）")
    for s, c in list(conflicts.items())[:20]:
        print("  分歧:", s[:50].replace("\n", " "), "->", list(c))
    if not args.dry_run:
        open(args.file, "w", encoding="utf-8", newline="").write(out)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
