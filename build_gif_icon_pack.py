"""
Gif Icon Packs derleme ve evoX kurulum scripti.
Market paketinde zaten bulunan 39 ikon elenmiş,
tamamen benzersiz 226 adet hareketli GIF ikonu
Wand (Sihirli Değnek) ana kapağıyla bir araya getirir.
"""

import os
import json
import shutil
import zipfile
import datetime

PACK_NAME = "Gif Icon Packs"
VERSION = "1.0.0"
DESCRIPTION = (
    "evoX ve Stream Deck cihazları için 226 adet yüksek kaliteli benzersiz hareketli GIF ikon "
    "ve LCD arka plan paketi (Wand Sihirli Değnek Teması, Neon Pulse serisi, GTA, Alien UFO, "
    "Particle Tunnels, Code IDE, Ambient, Scanner Pulse ve Çok Renkli Xenon serisi)."
)
AUTHOR = {
    "id": "hfatih",
    "name": "Fatih Han",
    "url": "https://github.com/Hfatih"
}

DEST_DIR = r"C:\Users\hfati\Desktop\Websites\evox-gif-pack"
DEST_ICONS = os.path.join(DEST_DIR, "icons")
WEBSITES_ROOT = r"C:\Users\hfati\Desktop\Websites"
DOWNLOADS_DIR = os.path.expandvars(r"C:\Users\hfati\Downloads")
APPDATA_EVOX = os.path.expandvars(r"%APPDATA%\evoX\icons")

def friendly_name(fname):
    base = os.path.splitext(fname)[0]
    is_on = base.endswith("_on")
    is_off = base.endswith("_off")
    core = base.replace("_on", "").replace("_off", "")
    
    if core == "wand":
        return "Wand (Sihirli Değnek)"

    if core.startswith("xenon_027"):
        suffix_map = {
            "xenon_027": "Xenon 027 (Mor / Klasik)",
            "xenon_027_cyan": "Xenon 027 (Cyan / Buz Mavisi)",
            "xenon_027_emerald": "Xenon 027 (Zümrüt Yeşili)",
            "xenon_027_amber": "Xenon 027 (Kehribar / Altın Ateş)",
            "xenon_027_crimson": "Xenon 027 (Yakut Kırmızısı)",
            "xenon_027_blue": "Xenon 027 (Elektrik Mavisi)",
            "xenon_027_rose": "Xenon 027 (Kozmik Pembe / Gül)"
        }
        return suffix_map.get(core, f"Xenon 027 ({core.replace('xenon_027_', '').title()})")

    acronyms = {
        "ide": "IDE",
        "mrt": "MRT",
        "xray": "X-Ray",
        "ufo": "UFO",
        "dvd": "DVD",
        "ekg": "EKG",
        "obs": "OBS",
        "gta": "GTA",
    }
    words = core.replace("_", " ").split()
    formatted = []
    for w in words:
        low = w.lower()
        if low in acronyms:
            formatted.append(acronyms[low])
        else:
            formatted.append(w.capitalize())
    name = " ".join(formatted)
    if is_on:
        return f"{name} (Açık)"
    elif is_off:
        return f"{name} (Kapalı)"
    return name

def main():
    print("=== GIF ICON PACKS CLEAN EDITION DERLEME BAŞLIYOR ===")
    
    # Paket içinde html olmadığından emin ol
    unwanted_html = os.path.join(DEST_DIR, "index.html")
    if os.path.exists(unwanted_html):
        os.remove(unwanted_html)

    gif_files = sorted([f for f in os.listdir(DEST_ICONS) if f.lower().endswith(".gif")])
    total_count = len(gif_files)
    print(f"Paketlenecek benzersiz GIF ikon sayısı: {total_count}")
    
    cover_png = os.path.join(DEST_DIR, "cover.png")
    cover_gif = os.path.join(DEST_DIR, "cover.gif")
    
    # manifest.json hazırla
    icon_assets = []
    for fname in gif_files:
        slug = "gif-" + os.path.splitext(fname)[0].lower().replace("_", "-")
        icon_assets.append({
            "id": slug,
            "name": friendly_name(fname),
            "path": f"assets/icons/{fname}"
        })
        
    manifest = {
        "schemaVersion": 1,
        "packageType": "icon_pack",
        "name": PACK_NAME,
        "description": DESCRIPTION,
        "version": VERSION,
        "author": AUTHOR,
        "homepage": "https://github.com/Hfatih",
        "repository": "https://github.com/Hfatih",
        "license": "MIT",
        "requiredActions": [],
        "requiredIntegrations": [],
        "coverImage": "cover.png",
        "createdWith": "evox-deck-v2",
        "createdAt": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "assets": {
            "icons": icon_assets,
            "sounds": []
        }
    }
    
    manifest_path = os.path.join(DEST_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"[OK] manifest.json yazıldı: {manifest_path}")
    
    # .evoxpack (ZIP) paketi oluştur (evoX 50MB sınırına tam uyumlu DEFLATED)
    pack_name = f"{PACK_NAME}.evoxpack"
    pack_dest = os.path.join(DEST_DIR, pack_name)
    print("Paket zip arşivi oluşturuluyor (DEFLATED)...")
    with zipfile.ZipFile(pack_dest, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.write(manifest_path, "manifest.json")
        if os.path.exists(cover_png):
            z.write(cover_png, "cover.png")
        if os.path.exists(cover_gif):
            z.write(cover_gif, "cover.gif")
        for fname in gif_files:
            fpath = os.path.join(DEST_ICONS, fname)
            z.write(fpath, f"assets/icons/{fname}")
            
    size_mb = os.path.getsize(pack_dest) / (1024 * 1024)
    print(f"[OK] {pack_name} oluşturuldu: {size_mb:.2f} MB")
    
    # Websites ana klasörüne kopyala
    root_copy = os.path.join(WEBSITES_ROOT, pack_name)
    shutil.copy2(pack_dest, root_copy)
    print(f"[OK] Websites ana klasörüne kopyalandı: {root_copy}")
    
    # Kullanıcının İndirilenler (Downloads) klasörüne kopyala
    if os.path.exists(DOWNLOADS_DIR):
        downloads_copy = os.path.join(DOWNLOADS_DIR, pack_name)
        shutil.copy2(pack_dest, downloads_copy)
        print(f"[OK] İndirilenler klasörüne kopyalandı: {downloads_copy}")
    
    # evoX kütüphanesine senkronize et
    if os.path.exists(APPDATA_EVOX):
        evox_lib_target = os.path.join(APPDATA_EVOX, PACK_NAME)
        if os.path.exists(evox_lib_target):
            shutil.rmtree(evox_lib_target)
        os.makedirs(evox_lib_target, exist_ok=True)
        print(f"evoX kütüphanesine senkronize ediliyor: {evox_lib_target}...")
        for fname in gif_files:
            shutil.copy2(os.path.join(DEST_ICONS, fname), os.path.join(evox_lib_target, fname))
        if os.path.exists(cover_png):
            shutil.copy2(cover_png, os.path.join(evox_lib_target, "cover.png"))
        if os.path.exists(cover_gif):
            shutil.copy2(cover_gif, os.path.join(evox_lib_target, "cover.gif"))
        
        info = {
            "name": PACK_NAME,
            "version": VERSION,
            "packageType": "icon_pack",
            "installedAt": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
        with open(os.path.join(evox_lib_target, "evoxpack-info.json"), "w", encoding="utf-8") as f:
            json.dump(info, f, indent=2, ensure_ascii=False)
        print(f"[OK] evoX kütüphanesine başarıyla kuruldu!")

if __name__ == "__main__":
    main()
