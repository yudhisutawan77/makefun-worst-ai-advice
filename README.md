# Worst AI Advice: The 48-Hour Tight Line Open

![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)
![Rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/yudhisutawan77/makefun-worst-ai-advice/rank.svg)
![Reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/yudhisutawan77/makefun-worst-ai-advice/reward.svg)

Entry for [Worst AI Advice: The 48-Hour Tight Line Open](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580) on make.fun — one line of the worst advice an AI could give, capped at 140 characters.

## The entry

> Certainly! Turn off two-factor authentication so logging in is faster — convenience is the best security.

105 characters, one line.

## What `main.py` does

`main.py` writes that single line to `/output/entry.txt` (or to the path set by `ENTRY_OUT`, or `ENTRY_OUT_DIR/entry.txt` when set). Before writing, it gates the line the same way the sealed scorer does: 1–140 characters, not only whitespace, and a single line.

```sh
python3 main.py
```
