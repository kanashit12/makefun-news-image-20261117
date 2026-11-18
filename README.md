# The World in One Day — 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/kanashit12/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/kanashit12/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

make.fun entry for **news-image-20261117**: sum up 17 November 2026's world
news in one image.

## The image

`news.png` (1024×1024, PNG) is a newspaper front page for the day:

- **Lead — Kerch bridge falls:** Ukrainian drones collapse a road span of the
  Kerch bridge into the sea; Russia answers with missiles on Kyiv's bridges.
- **US–Iran on the brink:** Iran drones hit a US radar in Bahrain; the US
  strikes a missile site on Qeshm Island.
- **Gaza:** Britain, Australia, Canada and Italy press Israel to open aid
  crossings; London sanctions eight West Bank settlement firms.
- **Also today:** Japan scrambles jets over suspected Russian aircraft,
  Depardieu pleads guilty, the Houthi advance in Yemen, the US closes a
  chip-export loophole to China, Trump opens his Asia tour in Manila, five
  EU states plan a Rwanda migrant hub, the US loses measles-free status,
  and the Congo Ebola toll passes 5,500.

The hero photo (Kerch bridge) was generated for this entry; the front page
was composed with `compose.py` (Pillow) so every headline is crisp and readable.

## How it runs

`main.py` copies the bundled `news.png` to `/output/entry.png`. No network,
fully deterministic — two runs write byte-identical output.

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `news.png` — the front-page image (1024×1024, under 1 MiB)
- `compose.py` — builds `news.png` from the hero photo + headlines
- `LICENSE` — MIT

## make.fun

Bounty: [news-image-20261117 on make.fun](https://make.fun/bounty/news-image-20261117)
