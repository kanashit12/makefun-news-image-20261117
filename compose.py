"""Build the 17 Nov 2026 front page (1024x1024 PNG) from the hero photo.

Layout: masthead, hero photo with caption, lead story, 2x2 story grid,
ticker strip, footer. All text is drawn with PIL so the page is readable
at a glance; the hero is the only photographic element.
"""
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
W, H = 1024, 1024
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, width, fill="black", leading=4):
    lines = wrap(draw, text, fnt, width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def main():
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline="black", width=4)

    # Masthead
    d.text((512, 18), "THE WORLD IN ONE DAY", font=font(SERIF_B, 58),
           fill="black", anchor="ma")
    d.text((512, 92), "TUESDAY 17 NOVEMBER 2026  •  TEN STORIES, ONE PAGE",
           font=font(SANS_B, 20), fill="black", anchor="ma")
    d.line([(24, 128), (1000, 128)], fill="black", width=3)

    # Hero photo
    hero = Image.open(HERE / "media-generation-hero-kerch-17nov-0-357af6cf-c1d8-43b7-adf4-132450521163.png").convert("RGB")
    # centre-crop to 976 x 300
    tw, th = 976, 300
    ratio = max(tw / hero.width, th / hero.height)
    hero = hero.resize((int(hero.width * ratio) + 1, int(hero.height * ratio) + 1))
    x0 = (hero.width - tw) // 2
    y0 = (hero.height - th) // 2
    hero = hero.crop((x0, y0, x0 + tw, y0 + th))
    img.paste(hero, (24, 140))
    d.rectangle([24, 140, 1000, 440], outline="black", width=2)
    d.text((24, 448), "A span of the Kerch bridge lies in the sea after the overnight strike.",
           font=font(SANS, 17), fill="#333333")

    # Lead story
    y = draw_wrapped(d, 24, 478, "KERCH BRIDGE FALLS: UKRAINE DRONES COLLAPSE A SPAN INTO THE SEA",
                     font(SERIF_B, 34), 976, leading=2)
    y = draw_wrapped(d, 24, y + 2,
                     "Kyiv calls it an unprecedented operation: 306 drones hit the crossing to "
                     "Crimea, halting road traffic. Russia answers with missiles on Kyiv's bridges.",
                     font(SERIF, 21), 976, leading=2)

    d.line([(24, y + 10), (1000, y + 10)], fill="black", width=2)
    gy = y + 22

    # 2x2 grid of stories
    stories = [
        ("US-IRAN ON THE BRINK",
         "Iran drones hit a US radar in Bahrain; the US strikes a missile site on "
         "Qeshm Island. Washington weighs a 'dirty bomb' claim against Tehran."),
        ("GAZA: OPEN THE CROSSINGS",
         "Britain, Australia, Canada and Italy press Israel to let aid in. London "
         "sanctions eight firms building West Bank settlements."),
        ("JAPAN SCRAMBLES JETS",
         "Tokyo protests after suspected Russian aircraft enter its airspace near "
         "Fukuoka, the latest in a week of close encounters."),
        ("DEPARDIEU PLEADS GUILTY",
         "Gerard Depardieu admits sexual assault and drops his appeal, ending one "
         "of France's most-watched celebrity trials."),
    ]
    col_w, row_h = 478, 132
    for i, (head, body) in enumerate(stories):
        cx = 24 + (i % 2) * 498
        cy = gy + (i // 2) * row_h
        if i % 2 == 1:
            d.line([(512, cy), (512, cy + row_h - 14)], fill="#999999", width=1)
        draw_wrapped(d, cx, cy, head, font(SANS_B, 21), col_w, leading=1)
        draw_wrapped(d, cx, cy + 30, body, font(SANS, 17), col_w, leading=1)

    ty = gy + 2 * row_h + 6
    d.line([(24, ty), (1000, ty)], fill="black", width=2)
    ticker = ("ALSO TODAY:  Trump opens Asia tour in Manila  •  Houthis advance in Yemen  •  "
              "US closes chip-export loophole to China  •  Five EU states plan Rwanda migrant hub  •  "
              "US loses measles-free status after 26 years  •  Congo Ebola toll passes 5,500")
    ty = draw_wrapped(d, 24, ty + 10, ticker, font(SANS_B, 17), 976, leading=3)
    d.text((512, 992), "THE WORLD IN ONE DAY — 17 NOVEMBER 2026",
           font=font(SANS, 15), fill="#555555", anchor="ma")
    img.save(HERE / "news.png", optimize=True)
    print("wrote", HERE / "news.png", (HERE / "news.png").stat().st_size)


if __name__ == "__main__":
    main()
