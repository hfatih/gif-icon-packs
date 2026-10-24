"""
Generate 6 color variations for xenon_027.gif
"""
import os
from PIL import Image, ImageSequence
import numpy as np
import cv2

ICONS_DIR = r"C:\Users\hfati\Desktop\Websites\evox-gif-pack\icons"
SRC_XENON = os.path.join(ICONS_DIR, "xenon_027.gif")

VARIATIONS = [
    # (suffix, name, hue_shift_0_to_179)
    # Original Xenon hue is ~136 (Violet/Purple)
    ("_cyan", "Cyan / Buz Mavisi", 134),       # ~90 (Cyan)
    ("_emerald", "Zümrüt Yeşili", 104),        # ~60 (Green)
    ("_amber", "Kehribar / Altın Ateş", 62),   # ~18 (Gold/Orange)
    ("_crimson", "Yakut Kırmızısı", 40),       # ~176 (Crimson Red)
    ("_blue", "Kobalt / Elektrik Mavisi", 154),# ~110 (Electric Blue)
    ("_rose", "Kozmik Pembe / Gül", 19),       # ~155 (Magenta/Rose)
]

def main():
    if not os.path.exists(SRC_XENON):
        print(f"Error: {SRC_XENON} not found")
        return

    im = Image.open(SRC_XENON)
    duration = im.info.get("duration", 30)
    print("Reading original frames...")
    
    # Pre-extract RGB arrays
    raw_rgb_frames = []
    for frame in ImageSequence.Iterator(im):
        raw_rgb_frames.append(np.array(frame.convert("RGB")))
        
    print(f"Read {len(raw_rgb_frames)} frames. Generating variations...")
    
    for suffix, label, shift in VARIATIONS:
        out_name = f"xenon_027{suffix}.gif"
        out_path = os.path.join(ICONS_DIR, out_name)
        
        new_frames = []
        for rgb in raw_rgb_frames:
            hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
            hsv[:, :, 0] = (hsv[:, :, 0].astype(int) + shift) % 180
            new_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
            new_frames.append(Image.fromarray(new_rgb).convert("P", palette=Image.Palette.ADAPTIVE))
            
        new_frames[0].save(
            out_path,
            save_all=True,
            append_images=new_frames[1:],
            loop=0,
            duration=duration,
            optimize=False
        )
        size_kb = os.path.getsize(out_path) / 1024
        print(f"[OK] {out_name} ({label}) -> {size_kb:.1f} KB")

if __name__ == "__main__":
    main()
