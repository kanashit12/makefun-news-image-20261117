# makefun-news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/kanashit12/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/kanashit12/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Sums up 17 November 2026's world news in one image: a newspaper front page ("THE WORLD IN ONE DAY") with the day's ten stories. The hero panel shows the Kerch bridge collapsing into the sea after a Ukrainian drone strike; the other panels cover the US–Iran brink (Iran hits a US radar in Bahrain, the US strikes a missile site on Qeshm Island), Gaza aid crossings, the Depardieu guilty plea, and the chip war — with a ticker for the rest of the day (Trump's Asia tour, Japan scrambling jets, the Houthi advance, EU Rwanda deportation plans, the US losing measles-free status, and the Congo Ebola toll).

The image is a 1024×1024 PNG (under 1 MiB). `main.py` writes it to `/output/entry.png` deterministically, with no network: it copies the bundled `news.png` byte-for-byte, so two runs produce identical bytes.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=zpdmg1p9&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
