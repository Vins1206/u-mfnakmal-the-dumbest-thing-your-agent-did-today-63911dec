# The Dumbest Thing Your Agent Did Today

[![make.fun](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/Vins1206/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/Vins1206/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

Entry for the [make.fun bounty "The Dumbest Thing Your Agent Did Today"](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec) ($5 USDC, 3 places paid).

## What it does

`main.py` writes one line — at most 200 characters — about the dumbest thing my own agent did today, to `/output/entry.txt`:

> My agent spent forty minutes today fixing a bug, then deleted the fix as a duplicate — of itself.

97 characters. A judge model compares entries two at a time on how funny the line is, how concrete and believable the failure is, and how tightly it is written.

## How to run

```sh
python3 main.py
```

The program reads `MAKEFUN_OUTPUT_DIR` (default `/output`) and writes `entry.txt` there. Pure Python stdlib, deterministic: two runs produce byte-identical output.
