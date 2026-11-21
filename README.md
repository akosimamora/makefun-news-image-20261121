# makefun-news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/akosimamora/makefun-news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/akosimamora/makefun-news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image summing up the world's news of Saturday, 21 November 2026: a 6.7 quake rattling Peru, COP31 running past its deadline with no deal, Antonelli fastest in Las Vegas qualifying but a penalty handing pole to Verstappen — plus 32 more stories from the day across 7 regions, with a pinned world map, a KPI strip and a DATE CHECK box explaining what was deliberately left out. The front page is drawn programmatically (PIL + DejaVu); the program itself just copies the bundled image to the output directory.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024 PNG, 169,109 bytes)
```

`main.py` runs on Python 3.13, standard library only, no network. It resolves `entry.png` against its own directory, never the working directory, verifies the PNG magic, dimensions, size and SHA-256, and writes byte-identical output on every run.

## Sources

Reuters · AP · AFP · Cricinfo · PTI · FIFA · FIA · Formula 1 · ESA · The Curtain · NYT · The Telegraph — every story checked against its original reporting on 21 November 2026. See NEWS.md for the story-by-story list.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1nmmcbpw&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
