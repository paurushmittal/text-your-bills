#!/usr/bin/env python3
"""Generate og.png (1200x630). Usage: python3 make_og.py [BrandName]"""
import sys
from PIL import Image, ImageDraw, ImageFont
BRAND = sys.argv[1] if len(sys.argv) > 1 else "Mabel"
INTER = "/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf"
BG, INK, INK2, ACC, SOFT = (251,248,243), (27,23,18), (90,81,70), (239,91,43), (253,232,222)
S = 2; W, H = 1200*S, 630*S
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
def font(size, w):
    try:
        f = ImageFont.truetype(INTER, size*S); f.set_variation_by_axes([32, w] if len(f.get_variation_axes())==2 else [w]); return f
    except Exception:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size*S)
# glow
d.ellipse([760*S, -160*S, 1460*S, 540*S], fill=SOFT)
# logo mark
x, y = 80*S, 78*S; m = 64*S
d.rounded_rectangle([x, y, x+m, y+m], radius=19*S, fill=ACC)
d.line([(x+19*S, y+34*S), (x+28*S, y+43*S), (x+47*S, y+23*S)], fill="white", width=7*S, joint="curve")
d.text((x+m+20*S, y+m/2), BRAND, font=font(46, 760), fill=INK, anchor="lm")
# headline
f1 = font(78, 760)
d.text((80*S, 225*S), "Text us your bills.", font=f1, fill=INK)
d.text((80*S, 318*S), "We handle the rest.", font=f1, fill=ACC)
f2 = font(30, 450)
d.text((82*S, 446*S), "We find the savings and handle the annoying calls.", font=f2, fill=INK2)
# chips
fx = font(24, 600); cx = 80*S; cy = 520*S
for t in ["No bank login", "No app", "Free to try"]:
    tw = d.textlength(t, font=fx); w = tw + 64*S
    d.rounded_rectangle([cx, cy, cx+w, cy+50*S], radius=25*S, fill="white", outline=(231,223,211), width=2*S)
    d.ellipse([cx+20*S, cy+19*S, cx+32*S, cy+31*S], fill=ACC)
    d.text((cx+42*S, cy+25*S), t, font=fx, fill=INK, anchor="lm"); cx += w + 14*S
# message bubbles (right)
fb = font(26, 500)
def bubble(x2, y, text, me):
    tw = d.textlength(text, font=fb); w = tw + 44*S
    x1 = x2 - w if me else x2
    box = [x1, y, x1+w, y+58*S]
    d.rounded_rectangle(box, radius=29*S, fill=(10,132,255) if me else (233,233,235))
    d.text((x1+22*S, y+29*S), text, font=fb, fill="white" if me else "black", anchor="lm")
bubble(1120*S, 120*S, "Here's my internet bill", True)
bubble(800*S, 196*S, "Got it! Digging in now", False)
bubble(1120*S, 272*S, "yes pls", True)
im = im.resize((1200, 630), Image.LANCZOS); im.save("og.png", optimize=True)
print("wrote og.png for", BRAND)
