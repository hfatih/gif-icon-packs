"""
Optimize all heavy GIFs in evox-gif-pack so total package is strictly < 50 MB
(evoX maxCompressedBytes hard limit).
"""

import os
from PIL import Image, ImageSequence

ICONS_DIR = r"C:\Users\hfati\Desktop\Websites\evox-gif-pack\icons"

def optimize_gif(file_path, max_frames=36):
    try:
        sz = os.path.getsize(file_path)
        if sz <= 240 * 1024:
            return False # already small enough
            
        with Image.open(file_path) as im:
            n_frames = getattr(im, "n_frames", 1)
            if n_frames <= max_frames:
                return False
                
            orig_dur = im.info.get("duration", 30)
            if orig_dur <= 0:
                orig_dur = 30
                
            step = max(1, n_frames // max_frames)
            selected_frames = []
            for i, frame in enumerate(ImageSequence.Iterator(im)):
                if i % step == 0 and len(selected_frames) < max_frames:
                    selected_frames.append(frame.copy())
                    
        # File is now closed!
        if not selected_frames:
            return False
            
        new_dur = orig_dur * step
        temp_path = file_path + ".temp.gif"
        selected_frames[0].save(
            temp_path,
            format="GIF",
            save_all=True,
            append_images=selected_frames[1:],
            loop=0,
            duration=new_dur,
            optimize=True
        )
        
        new_sz = os.path.getsize(temp_path)
        if new_sz < sz:
            os.replace(temp_path, file_path)
            print(f"Optimized {os.path.basename(file_path)}: {sz//1024}KB -> {new_sz//1024}KB")
            return True
        else:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            return False
    except Exception as e:
        print(f"Error optimizing {file_path}: {e}")
        return False

def main():
    print("=== OPTIMIZING GIF ICONS TO FIT UNDER 50 MB ===")
    files = sorted([f for f in os.listdir(ICONS_DIR) if f.endswith(".gif")])
    print(f"Total icons to process: {len(files)}")
    
    optimized_count = 0
    for idx, f in enumerate(files):
        fp = os.path.join(ICONS_DIR, f)
        if optimize_gif(fp, max_frames=36):
            optimized_count += 1
            
    print(f"Optimized {optimized_count} heavy GIFs.")
    
    total_uncompressed = sum(os.path.getsize(os.path.join(ICONS_DIR, f)) for f in files)
    print(f"Total uncompressed size: {total_uncompressed / (1024*1024):.2f} MB")

if __name__ == "__main__":
    main()
