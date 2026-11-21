# Saturday 21 November 2026, in one image

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/akosimamora/makefun-news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/akosimamora/makefun-news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A newspaper front page for Saturday, 21 November 2026. The big stories of
the day lead: a magnitude 6.7 earthquake shaking Peru, the COP31 climate
talks running past their deadline with no deal, and Antonelli quickest in
Las Vegas qualifying before a penalty hands pole to Verstappen. Around them,
32 more stories from the day across 7 regions, a KPI strip, a region bar, a
world map with numbered pins, and a DATE CHECK box that says plainly what
was left out and why.

The page is drawn programmatically (PIL + DejaVu, from the verified stories
in NEWS.md). The program in this repository does not draw it — it copies the
bundled `entry.png` to the output directory, after checking the PNG magic,
the 1024x1024 size, the byte count and the SHA-256.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png — 1024x1024 PNG, 171,131 bytes
```

`main.py` needs Python 3.13 and the standard library only. No network, no
clock, no randomness: every run writes the same bytes.

## Where the news comes from

Reuters, AP, AFP, Cricinfo, PTI, FIFA, FIA, Formula 1, ESA, The Curtain,
NYT, The Telegraph. Every story was checked against its original reporting
on 21 November 2026; the story-by-story list is in NEWS.md.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1nmmcbpw&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
