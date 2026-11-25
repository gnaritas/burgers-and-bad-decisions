#!/usr/bin/env python3
"""og.png 1200x630 — Burgers & Bad Decisions — late-night ticket poster.
Charcoal ink, milkshake cream, mustard rules, ketchup red, arcade mint. Shop identity only.
Every line is measured and center-fitted; the script FAILS if any line would collide."""
from PIL import Image, ImageDraw, ImageFont
import os, sys

W, H = 1200, 630
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "og.png")

INK = (29, 25, 21); INK2 = (20, 17, 16); CREAM = (245, 236, 216)
MUSTARD = (232, 178, 60); RED = (200, 68, 58); SMOKE = (162, 151, 134); MINT = (138, 210, 168)

def font(paths, size):
    bases = ["/System/Library/Fonts/Supplemental/", "/System/Library/Fonts/"]
    for b in bases:
        for n in paths:
            p = b + n
            if os.path.exists(p):
                try: return ImageFont.truetype(p, size)
                except Exception: pass
    return ImageFont.load_default()

serif = lambda s: font(["Iowan Old Style.ttc", "Palatino.ttc", "Georgia.ttf", "Times New Roman.ttf"], s)
sans = lambda s: font(["Futura.ttc", "HelveticaNeue.ttc", "Arial Bold.ttf", "Arial.ttf"], s)
mono = lambda s: font(["Menlo.ttc", "Consolas", "Monaco.dfont", "Courier New.ttf"], s)

img = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(img)

# lower band = the counter-top (ink2)
d.rectangle([0, 486, W, H], fill=INK2)
# mustard rails top + bottom
d.rectangle([0, 0, W, 7], fill=MUSTARD)
d.rectangle([0, H-7, W, H], fill=MUSTARD)

widths = []
def center(text, f, y, fill, tracking=0):
    if tracking:
        cw = [d.textbbox((0,0), ch, font=f)[2]-d.textbbox((0,0), ch, font=f)[0] for ch in text]
        tw = sum(cw) + tracking*(len(text)-1)
        x = (W-tw)/2
        for ch,w_ in zip(text,cw):
            bb = d.textbbox((0,0), ch, font=f)
            d.text((x - bb[0], y), ch, font=f, fill=fill)
            x += w_ + tracking
        widths.append((y, tw))
        return tw
    bb = d.textbbox((0,0), text, font=f)
    tw = bb[2]-bb[0]
    d.text(((W-tw)/2 - bb[0], y), text, font=f, fill=fill)
    widths.append((y, tw))
    return tw

# kicker
center("OPENING SOON  ·  68 MAIN STREET  ·  DOWNTOWN BANGOR, MAINE", mono(23), 46, MUSTARD, tracking=5)

# brand — two stacked lines, red "&"
center("BURGERS &", sans(102), 100, CREAM)
center("BAD DECISIONS", sans(102), 218, RED)

# dashed ticket rule under brand
for i in range(0, 280, 22):
    x = W/2 - 140 + i
    d.rectangle([x, 352, x+13, 355], fill=MUSTARD)

# line
center("Breakfast from sunrise.", serif(46), 378, CREAM)
center("Loaded burgers at midnight.", serif(46), 438, MUSTARD)

# ticket strip on the counter band — measured, single rows, no side elements to collide with
center("The Classic Mistake  ·  The Bad Decision  ·  The Hangover Burger", sans(26), 506, CREAM)
center("Breakfast all day  ·  Veg option on everything  ·  NA version of every drink", mono(21), 548, MINT)
center("A locally owned burger bar in the old Taste of India space — opening soon", mono(21), 584, SMOKE)

img.save(OUT, "PNG", optimize=True)

# collision guard: no line may exceed the safe box (W-80)
bad = [(y, tw) for y, tw in widths if tw > W-80]
if bad:
    for y, tw in bad: print("OVERWIDE", y, tw, file=sys.stderr)
    sys.exit(1)
print("wrote", OUT, os.path.getsize(OUT), "bytes; widest line:", max(tw for _, tw in widths), "px (safe box", W-80, ")")
