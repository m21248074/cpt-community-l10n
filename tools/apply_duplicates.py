#!/usr/bin/env python3
"""把已翻譯的字串套用到「原文完全相同」但尚未翻譯的項目。

只在同一原文的所有既有譯文一致時才套用；有分歧的原文會列出供人工處理。
套用後的項目移除 type="unfinished"。

分歧的原文可用 --prefer 原文=譯文 指定統一譯名，會覆寫該原文所有既有譯文。

用法：python tools/apply_duplicates.py [--dry-run] [--prefer 原文=譯文 ...] [檔案]
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
    ap.add_argument("--prefer", action="append", default=[], metavar="原文=譯文")
    args = ap.parse_args()

    text = open(args.file, encoding="utf-8", newline="").read()

    known = collections.defaultdict(collections.Counter)
    for m in MSG.finditer(text):
        s, t = SRC.search(m.group(0)), TR.search(m.group(0))
        if s and t and "numerus" not in m.group(0)[:60] and CJK.search(t.group(2)):
            known[s.group(1)][t.group(2)] += 1

    prefer = dict(p.split("=", 1) for p in args.prefer)
    for s, tr in prefer.items():
        known[s] = collections.Counter({tr: 1})
    conflicts = {s: c for s, c in known.items() if len(c) > 1}
    applied = 0

    def repl(m):
        nonlocal applied
        block = m.group(0)
        s, t = SRC.search(block), TR.search(block)
        if not (s and t) or "numerus=" in block.split(">", 1)[0]:
            return block
        src = s.group(1)
        if src in prefer:
            new = prefer[src]
            if t.group(2) == new and not t.group(1).strip():
                return block
        elif CJK.search(t.group(2)) or src not in known or src in conflicts:
            return block
        else:
            new = next(iter(known[src]))
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
