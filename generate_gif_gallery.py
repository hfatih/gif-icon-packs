"""
Gif Icon Packs Stream Deck 15-Tuşlu İnteraktif Simülatör ve Galeri Üretici (226 İkon)
"""

import os
import json

ICONS_DIR = r"C:\Users\hfati\Desktop\Websites\evox-gif-pack\icons"
OUT_HTML_ROOT = r"C:\Users\hfati\Desktop\Websites\gif_icons_gallery.html"

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
        "vfx": "VFX",
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

def categorize(fname):
    low = fname.lower()
    if low.startswith("xenon_027"):
        return "Xenon Serisi"
    elif any(k in low for k in ['grand_theft_auto', 'test_drive', 'game_dice', 'dvd', 'alien']):
        return 'Retro Gaming & Klasikler'
    elif any(k in low for k in ['code_ide', 'terminal', 'chat', 'countdown']):
        return 'Developer & Kodlama'
    elif any(k in low for k in ['particle_tunnel', 'scan_pulse', 'glitch', 'balls', 'radioactive', 'biohazard', 'fluorescent', 'smoke', 'mrt_xray']):
        return 'Cyber, VFX & Partiküller'
    elif any(k in low for k in ['clouds', 'moon', 'rain', 'thunder', 'snow', 'sandstorm', 'palm_avenue', 'aquarium', 'jellyfish']):
        return 'Doğa & Ambient'
    elif any(k in low for k in ['discord', 'spotify', 'twitch', 'youtube', 'instagram', 'x.gif']):
        return 'Sosyal Medya & Markalar'
    elif any(k in low for k in ['mic', 'headphones', 'volume', 'audio', 'sound', 'play', 'pause', 'next', 'prev', 'repeat', 'shuffle', 'music']):
        return 'Medya & Ses'
    else:
        return 'Neon Kontroller & UI'

def build():
    files = sorted([f for f in os.listdir(ICONS_DIR) if f.lower().endswith(".gif")])
    print(f"Toplam GIF dosyası: {len(files)}")
    
    assets = []
    cat_counts = {}
    
    for f in files:
        cat = categorize(f)
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
        name = friendly_name(f)
        slug = "gif-" + os.path.splitext(f)[0].lower().replace("_", "-")
        assets.append({
            "id": slug,
            "name": name,
            "filename": f,
            "category": cat
        })
        
    initial_15 = [
        "wand.gif",
        "code_ide_001.gif",
        "particle_tunnel_001.gif",
        "spotify.gif",
        "xenon_027_cyan.gif",
        "grand_theft_auto.gif",
        "chat_001.gif",
        "xenon_027_amber.gif",
        "discord.gif",
        "alien_ufo_akte_x_i_want_to_believe.gif",
        "scan_pulse_002.gif",
        "xenon_027_emerald.gif",
        "heart_on.gif",
        "moon_reflection_001.gif",
        "xenon_027_crimson.gif"
    ]
    
    ordered_cats = [
        "Xenon Serisi",
        "Retro Gaming & Klasikler",
        "Developer & Kodlama",
        "Cyber, VFX & Partiküller",
        "Doğa & Ambient",
        "Medya & Ses",
        "Sosyal Medya & Markalar",
        "Neon Kontroller & UI"
    ]
    
    filter_tabs_html = f'<button class="filter-btn active" data-filter="all">Tümü ({len(assets)})</button>\n'
    for c in ordered_cats:
        cnt = cat_counts.get(c, 0)
        filter_tabs_html += f'      <button class="filter-btn" data-filter="{c}">{c} ({cnt})</button>\n'
        
    html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gif Icon Packs — 15 Tuşlu Stream Deck & evoX İnteraktif Simülatör</title>
  <meta name="description" content="226 Benzersiz Hareketli GIF İkonlu Stream Deck ve evoX Donanım Simülatörü ve Vitrin Galerisi.">
  <link rel="icon" type="image/png" href="evox-gif-pack/cover.png">
  <style>
    :root {{
      --bg: #0b070f;
      --panel: #160f1e;
      --card: #20152b;
      --card-hover: #2d1c3e;
      --accent: #f0abc5;
      --accent-secondary: #c084fc;
      --accent-glow: rgba(240, 171, 197, 0.45);
      --purple-glow: rgba(192, 132, 252, 0.35);
      --text: #fdf2f8;
      --text-muted: #d8b4e2;
      --border: #3b2552;
      --border-focus: #e7a0b9;
      --deck-body: #100a18;
      --deck-bezel: #251733;
      --key-border: #44285e;
      --key-glow: 0 0 16px rgba(240, 171, 197, 0.4);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg);
      background-image: radial-gradient(circle at 50% 0%, #261239 0%, #0b070f 75%);
      color: var(--text);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}
    
    header {{
      background: rgba(22, 15, 30, 0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 1.1rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 1rem;
    }}
    .brand-logo-wrap {{
      width: 48px;
      height: 48px;
      border-radius: 12px;
      background: linear-gradient(135deg, #f0abc5, #9333ea);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 16px var(--accent-glow);
      font-size: 1.5rem;
      overflow: hidden;
      padding: 2px;
    }}
    .brand h1 {{
      font-size: 1.35rem;
      font-weight: 800;
      letter-spacing: -0.5px;
      background: linear-gradient(135deg, #fff, #f0abc5);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .brand p {{
      font-size: 0.82rem;
      color: var(--text-muted);
    }}
    .header-actions {{
      display: flex;
      gap: 0.75rem;
      align-items: center;
    }}
    .btn {{
      background: linear-gradient(135deg, #e7a0b9, #c084fc);
      color: #100a18;
      padding: 0.55rem 1.2rem;
      border-radius: 10px;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.88rem;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 15px var(--accent-glow);
    }}
    .btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 22px var(--accent-glow);
    }}
    .btn-outline {{
      background: rgba(32, 21, 43, 0.6);
      border: 1px solid var(--border);
      color: var(--text);
      box-shadow: none;
    }}
    .btn-outline:hover {{
      border-color: var(--accent);
      background: rgba(240, 171, 197, 0.12);
      color: #fff;
    }}
    
    main {{
      flex: 1;
      max-width: 1400px;
      margin: 0 auto;
      padding: 2.2rem 1.5rem;
      width: 100%;
    }}
    
    /* 15-KEY STREAM DECK HARDWARE SIMULATOR */
    .simulator-container {{
      background: linear-gradient(180deg, rgba(28, 18, 40, 0.85) 0%, rgba(18, 11, 26, 0.95) 100%);
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 2.2rem;
      margin-bottom: 2.8rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(255, 255, 255, 0.08);
      position: relative;
      overflow: hidden;
    }}
    .simulator-container::before {{
      content: "";
      position: absolute;
      top: -100px;
      left: 50%;
      transform: translateX(-50%);
      width: 450px;
      height: 200px;
      background: radial-gradient(ellipse, var(--purple-glow) 0%, transparent 70%);
      pointer-events: none;
    }}
    
    .sim-header {{
      text-align: center;
      margin-bottom: 1.8rem;
      position: relative;
      z-index: 2;
    }}
    .sim-badge {{
      display: inline-block;
      padding: 0.3rem 0.8rem;
      background: rgba(240, 171, 197, 0.15);
      border: 1px solid rgba(240, 171, 197, 0.35);
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--accent);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 0.6rem;
    }}
    .sim-header h2 {{
      font-size: 1.6rem;
      font-weight: 800;
      margin-bottom: 0.35rem;
      letter-spacing: -0.5px;
    }}
    .sim-header p {{
      font-size: 0.9rem;
      color: var(--text-muted);
    }}
    
    /* HARDWARE DECK CASING */
    .deck-frame {{
      background: linear-gradient(145deg, #181022, #0d0714);
      border: 3px solid var(--deck-bezel);
      border-radius: 28px;
      padding: 24px 26px;
      box-shadow: 
        inset 0 2px 10px rgba(255, 255, 255, 0.05),
        inset 0 -8px 20px rgba(0, 0, 0, 0.9),
        0 18px 45px rgba(0, 0, 0, 0.8),
        0 0 30px rgba(192, 132, 252, 0.15);
      position: relative;
    }}
    .deck-frame::after {{
      content: "STREAM DECK • EVOX";
      position: absolute;
      bottom: 8px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 0.65rem;
      letter-spacing: 2px;
      font-weight: 800;
      color: rgba(216, 180, 226, 0.35);
    }}
    
    /* 5 COLUMNS x 3 ROWS GRID = 15 KEYS */
    .deck-grid {{
      display: grid;
      grid-template-columns: repeat(5, 84px);
      grid-template-rows: repeat(3, 84px);
      gap: 14px;
      margin-bottom: 12px;
    }}
    
    .deck-key {{
      width: 84px;
      height: 84px;
      background: radial-gradient(circle at 50% 30%, #1e132b 0%, #0d0714 100%);
      border: 2px solid var(--key-border);
      border-radius: 16px;
      overflow: hidden;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
      position: relative;
      box-shadow: inset 0 2px 5px rgba(255, 255, 255, 0.08), 0 4px 10px rgba(0, 0, 0, 0.6);
    }}
    .deck-key:hover {{
      border-color: var(--accent);
      transform: translateY(-3px) scale(1.04);
      box-shadow: var(--key-glow), 0 8px 18px rgba(0, 0, 0, 0.8);
    }}
    .deck-key.active-slot {{
      border-color: #fff;
      box-shadow: 0 0 24px rgba(240, 171, 197, 0.9), inset 0 0 12px rgba(255, 255, 255, 0.4);
      transform: scale(1.06);
    }}
    .deck-key img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      pointer-events: none;
    }}
    .deck-key .slot-num {{
      position: absolute;
      top: 4px;
      left: 6px;
      font-size: 0.6rem;
      font-weight: 800;
      color: rgba(255, 255, 255, 0.45);
      background: rgba(0, 0, 0, 0.4);
      padding: 1px 4px;
      border-radius: 4px;
      pointer-events: none;
    }}
    
    .sim-controls {{
      margin-top: 1.4rem;
      display: flex;
      gap: 0.8rem;
      flex-wrap: wrap;
      justify-content: center;
    }}
    .sim-btn {{
      background: var(--card);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 0.45rem 1rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
    }}
    .sim-btn:hover {{
      background: var(--panel);
      color: var(--text);
      border-color: var(--accent);
    }}
    
    /* SEARCH AND FILTER BAR */
    .controls-panel {{
      margin-bottom: 2rem;
      display: flex;
      flex-direction: column;
      gap: 1.2rem;
    }}
    .search-input-wrap {{
      position: relative;
      width: 100%;
    }}
    .search-input {{
      width: 100%;
      background: var(--card);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 0.85rem 1.4rem 0.85rem 3rem;
      border-radius: 14px;
      font-size: 1rem;
      outline: none;
      transition: all 0.2s;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
    }}
    .search-input:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 16px var(--accent-glow);
    }}
    .search-icon {{
      position: absolute;
      left: 1.1rem;
      top: 50%;
      transform: translateY(-50%);
      font-size: 1.1rem;
      color: var(--text-muted);
      pointer-events: none;
    }}
    
    .filter-tabs {{
      display: flex;
      gap: 0.6rem;
      flex-wrap: wrap;
    }}
    .filter-btn {{
      background: var(--card);
      color: var(--text-muted);
      border: 1px solid var(--border);
      padding: 0.5rem 1.1rem;
      border-radius: 10px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .filter-btn:hover {{
      background: var(--panel);
      color: var(--text);
      border-color: var(--accent);
    }}
    .filter-btn.active {{
      background: linear-gradient(135deg, var(--accent), var(--accent-secondary));
      color: #100a18;
      border-color: transparent;
      font-weight: 700;
      box-shadow: 0 4px 12px var(--accent-glow);
    }}
    
    /* GALLERY GRID */
    .gallery-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.2rem;
    }}
    .gallery-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text);
    }}
    .gallery-count {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    
    .gallery-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(136px, 1fr));
      gap: 16px;
    }}
    .icon-card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 14px 10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 10px;
      text-align: center;
      transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
      cursor: pointer;
      position: relative;
      overflow: hidden;
    }}
    .icon-card:hover {{
      background: var(--card-hover);
      border-color: var(--accent);
      transform: translateY(-4px);
      box-shadow: 0 10px 24px rgba(0, 0, 0, 0.5), 0 0 16px var(--purple-glow);
    }}
    .icon-card .img-wrap {{
      width: 88px;
      height: 88px;
      border-radius: 14px;
      background: #100a18;
      border: 1px solid rgba(255, 255, 255, 0.05);
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .icon-card img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .icon-info {{
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 3px;
    }}
    .icon-name {{
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text);
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      width: 100%;
    }}
    .icon-category {{
      font-size: 0.68rem;
      color: var(--text-muted);
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      width: 100%;
    }}
    .hint-toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: rgba(22, 15, 30, 0.95);
      border: 1px solid var(--accent);
      color: var(--text);
      padding: 0.8rem 1.4rem;
      border-radius: 12px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7);
      font-size: 0.88rem;
      z-index: 1000;
      display: none;
      align-items: center;
      gap: 0.6rem;
      animation: fadeIn 0.3s ease;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(10px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    @media (max-width: 600px) {{
      .deck-grid {{
        grid-template-columns: repeat(5, 56px);
        grid-template-rows: repeat(3, 56px);
        gap: 8px;
      }}
      .deck-key {{
        width: 56px;
        height: 56px;
        border-radius: 10px;
      }}
      .gallery-grid {{
        grid-template-columns: repeat(auto-fill, minmax(105px, 1fr));
        gap: 10px;
      }}
      .icon-card .img-wrap {{
        width: 64px;
        height: 64px;
      }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="brand">
      <div class="brand-logo-wrap"><img src="evox-gif-pack/icons/wand.gif" alt="Wand" style="width:100%;height:100%;object-fit:cover;border-radius:10px;"></div>
      <div>
        <h1>Gif Icon Packs</h1>
        <p>226 Benzersiz Hareketli GIF İkon • Wand Sihirli Değnek Edition • Neon Pulse • Cyber VFX</p>
      </div>
    </div>
    <div class="header-actions">
      <a href="Gif Icon Packs.evoxpack" class="btn" download>📦 .evoxpack İndir (226 İkon - 33 MB)</a>
      <a href="atomic_peach_gallery.html" class="btn btn-outline">🍑 Atomic Peach Galerisi</a>
    </div>
  </header>

  <main>
    <!-- 15-KEY HARDWARE STREAM DECK SIMULATOR -->
    <div class="simulator-container">
      <div class="sim-header">
        <span class="sim-badge">15 Tuşlu Donanım Konsolu</span>
        <h2>Stream Deck & evoX Canlı Konsol Simülatörü</h2>
        <p>Aşağıdaki galeriden herhangi bir hareketli ikona tıklayarak seçili tuşa yerleştirin veya tuşları deneyin</p>
      </div>
      
      <div class="deck-frame">
        <div class="deck-grid" id="deckGrid"></div>
      </div>
      
      <div class="sim-controls">
        <button class="sim-btn" id="btnRandomFill">🎲 Rastgele 15 Tuş Doldur</button>
        <button class="sim-btn" id="btnResetDeck">↺ Varsayılana Sıfırla</button>
      </div>
    </div>

    <!-- CONTROLS & FILTER -->
    <div class="controls-panel">
      <div class="search-input-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="İkon ara (wand, xenon, ide, code, tunnel, discord, neon, gta, sound...)...">
      </div>

      <div class="filter-tabs" id="filterTabs">
{filter_tabs_html}      </div>
    </div>

    <!-- GALLERY GRID -->
    <div class="gallery-header">
      <div class="gallery-title" id="galleryTitle">Tüm İkonlar</div>
      <div class="gallery-count" id="galleryCount">226 İkon Gösteriliyor</div>
    </div>
    
    <div class="gallery-grid" id="galleryGrid"></div>
  </main>

  <div class="hint-toast" id="hintToast">
    <span style="font-size: 1.2rem;">✨</span>
    <span id="hintText">Tuş güncellendi!</span>
  </div>

  <script>
    const INITIAL_KEYS = {json.dumps(initial_15)};
    const ASSETS = {json.dumps(assets, ensure_ascii=False)};
    
    let activeSlotIndex = 0;

    function resolveImg(imgEl, filename) {{
      imgEl.onerror = function() {{
        if (!this.dataset.tried) {{
          this.dataset.tried = "1";
          this.src = "evox-gif-pack/icons/" + filename;
        }} else if (this.dataset.tried === "1") {{
          this.dataset.tried = "2";
          this.src = "icons/" + filename;
        }} else if (this.dataset.tried === "2") {{
          this.dataset.tried = "3";
          this.src = "../icons/" + filename;
        }}
      }};
      imgEl.src = "evox-gif-pack/icons/" + filename;
    }}

    function showToast(text) {{
      const toast = document.getElementById('hintToast');
      const toastText = document.getElementById('hintText');
      toastText.textContent = text;
      toast.style.display = 'flex';
      clearTimeout(window.toastTimer);
      window.toastTimer = setTimeout(() => {{
        toast.style.display = 'none';
      }}, 2200);
    }}

    const deckGrid = document.getElementById('deckGrid');
    
    function initDeck(keys) {{
      deckGrid.innerHTML = '';
      keys.forEach((k, idx) => {{
        const div = document.createElement('div');
        div.className = 'deck-key' + (idx === activeSlotIndex ? ' active-slot' : '');
        div.dataset.slot = idx;
        
        const slotNum = document.createElement('span');
        slotNum.className = 'slot-num';
        slotNum.textContent = (idx + 1);
        div.appendChild(slotNum);
        
        const img = document.createElement('img');
        img.alt = 'Key ' + (idx + 1);
        resolveImg(img, k);
        div.appendChild(img);
        
        div.onclick = () => {{
          document.querySelectorAll('.deck-key').forEach(k => k.classList.remove('active-slot'));
          div.classList.add('active-slot');
          activeSlotIndex = idx;
          showToast(`Tuş #${{idx + 1}} seçildi. Galeriden bir ikona tıklayın.`);
        }};
        
        deckGrid.appendChild(div);
      }});
    }}
    
    initDeck(INITIAL_KEYS);

    const galleryGrid = document.getElementById('galleryGrid');
    const galleryTitle = document.getElementById('galleryTitle');
    const galleryCount = document.getElementById('galleryCount');
    
    function renderGallery(items) {{
      galleryGrid.innerHTML = '';
      galleryCount.textContent = `${{items.length}} İkon Gösteriliyor`;
      
      items.forEach(item => {{
        const card = document.createElement('div');
        card.className = 'icon-card';
        card.title = `${{item.name}} — Tıkla ve Stream Deck #${{activeSlotIndex + 1}} tuşuna yerleştir`;
        
        const imgWrap = document.createElement('div');
        imgWrap.className = 'img-wrap';
        
        const img = document.createElement('img');
        img.alt = item.name;
        img.loading = "lazy";
        resolveImg(img, item.filename);
        imgWrap.appendChild(img);

        const info = document.createElement('div');
        info.className = 'icon-info';

        const nameDiv = document.createElement('div');
        nameDiv.className = 'icon-name';
        nameDiv.textContent = item.name;

        const catDiv = document.createElement('div');
        catDiv.className = 'icon-category';
        catDiv.textContent = item.category;

        info.appendChild(nameDiv);
        info.appendChild(catDiv);

        card.appendChild(imgWrap);
        card.appendChild(info);

        card.onclick = () => {{
          const allKeys = deckGrid.querySelectorAll('.deck-key');
          const targetKey = allKeys[activeSlotIndex] || allKeys[0];
          if (targetKey) {{
            const keyImg = targetKey.querySelector('img');
            resolveImg(keyImg, item.filename);
            
            targetKey.style.transform = 'scale(1.15)';
            setTimeout(() => {{
              targetKey.style.transform = '';
            }}, 200);
            
            showToast(`[Tuş #${{activeSlotIndex + 1}}] "${{item.name}}" yerleştirildi!`);
            
            allKeys.forEach(k => k.classList.remove('active-slot'));
            activeSlotIndex = (activeSlotIndex + 1) % 15;
            allKeys[activeSlotIndex].classList.add('active-slot');
          }}
        }};
        
        galleryGrid.appendChild(card);
      }});
    }}
    
    renderGallery(ASSETS);

    const searchInput = document.getElementById('searchInput');
    searchInput.oninput = (e) => {{
      const q = e.target.value.toLowerCase().trim();
      const filtered = ASSETS.filter(a => a.name.toLowerCase().includes(q) || a.category.toLowerCase().includes(q) || a.filename.toLowerCase().includes(q));
      renderGallery(filtered);
      if (q) {{
        galleryTitle.textContent = `Arama Sonuçları: "${{q}}"`;
      }} else {{
        galleryTitle.textContent = "Tüm İkonlar";
      }}
    }};

    document.querySelectorAll('.filter-btn').forEach(btn => {{
      btn.onclick = () => {{
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        searchInput.value = '';
        const f = btn.dataset.filter;
        if (f === 'all') {{
          galleryTitle.textContent = "Tüm İkonlar";
          renderGallery(ASSETS);
        }} else {{
          galleryTitle.textContent = f;
          renderGallery(ASSETS.filter(a => a.category === f));
        }}
      }};
    }});

    document.getElementById('btnResetDeck').onclick = () => {{
      activeSlotIndex = 0;
      initDeck(INITIAL_KEYS);
      showToast("Stream Deck varsayılan düzene sıfırlandı.");
    }};

    document.getElementById('btnRandomFill').onclick = () => {{
      const shuffled = [...ASSETS].sort(() => 0.5 - Math.random());
      const random15 = shuffled.slice(0, 15).map(a => a.filename);
      activeSlotIndex = 0;
      initDeck(random15);
      showToast("🎲 15 tuş rastgele GIF ikonlarla dolduruldu!");
    }};
  </script>
</body>
</html>
"""
    
    with open(OUT_HTML_ROOT, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[OK] Ana galeri HTML yazıldı: {OUT_HTML_ROOT}")

if __name__ == "__main__":
    build()
