# -*- coding: utf-8 -*-
"""set_coords.py — Cập nhật TOẠ ĐỘ CHÍNH XÁC từ link Google Maps / Yandex / plus-code / "lat,lon".

Cách dùng:
  1) Mở _sync/coords.txt, mỗi dòng: <slug hoặc tên địa điểm> => <link Google Maps hoặc "lat, lon">
     Ví dụ:
       chua-hang-luong => https://www.google.com/maps/place/.../@20.99,106.68,17z/data=...!3d20.9961776!4d106.6803944...
       Chùa Thiên Mụ   => 16.4534, 107.5546
  2) Chạy:  python3 tools/set_coords.py   (rồi python3 tools/build.py để build lại — script tự gọi luôn)

Ưu tiên lấy toạ độ ghim thật của Google: !3d<lat>!4d<lon>. Không cần đổi hệ quy chiếu — Google dùng WGS84
đúng như bản đồ web, chỉ cần đưa thẳng lat/lon (thập phân) vào là ghim đúng.
"""
import json, os, glob, re, sys, unicodedata

HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
REG=os.path.join(ROOT,"data","regions")
TXT=sys.argv[1] if len(sys.argv)>1 else os.path.join(ROOT,"_sync","coords.txt")

def parse_coord(v):
    v=v.strip()
    mm=re.findall(r'!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)', v)     # Google: lấy CẶP CUỐI (ghim thật của địa điểm; link có thể chứa điểm phụ)
    if mm: return float(mm[-1][0]), float(mm[-1][1])
    m=re.search(r'/@(-?\d+\.\d+),(-?\d+\.\d+)', v)          # Google: tâm khung nhìn
    if m: return float(m.group(1)), float(m.group(2))
    m=re.search(r'[?&]ll=(-?\d+\.\d+),(-?\d+\.\d+)', v)     # Yandex: ll=lon,lat
    if m: return float(m.group(2)), float(m.group(1))
    m=re.search(r'[?&#](?:q|query|ll|center)=(-?\d+\.\d+),\s*(-?\d+\.\d+)', v)
    if m: return float(m.group(1)), float(m.group(2))
    m=re.fullmatch(r'\s*(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\s*', v)   # "lat, lon"
    if m: return float(m.group(1)), float(m.group(2))
    return None

def nfc(s): return unicodedata.normalize("NFC",s or "")

def load_all():
    files={}; 
    for f in glob.glob(os.path.join(REG,"*.json")):
        files[f]=json.load(open(f,encoding="utf-8"))
    return files

def main():
    if not os.path.exists(TXT):
        print("Chưa có file:",TXT,"\nTạo file này, mỗi dòng: <slug hoặc tên> => <link Google Maps / lat,lon>"); return
    files=load_all()
    # index by slug and by normalized name
    idx_slug={}; idx_name={}
    for f,arr in files.items():
        for p in arr:
            idx_slug[p["slug"]]=(f,p)
            idx_name.setdefault(nfc(p.get("name_vi","")).lower().strip(),[]).append((f,p))
    updated=set(); done=0; miss=[]
    for ln in open(TXT,encoding="utf-8"):
        ln=ln.strip()
        if not ln or ln.startswith("#"): continue
        for sep in ["=>","\t","|","="]:
            if sep in ln: key,val=ln.split(sep,1); break
        else:
            print("  (bỏ qua, thiếu dấu =>):",ln[:50]); continue
        key=key.strip(); co=parse_coord(val)
        if not co: print("  (không đọc được toạ độ):",ln[:60]); continue
        la,lo=co
        target=None
        if key in idx_slug: target=idx_slug[key]
        elif nfc(key).lower().strip() in idx_name: target=idx_name[nfc(key).lower().strip()][0]
        else:
            for nm,lst in idx_name.items():
                if nfc(key).lower().strip() in nm: target=lst[0]; break
        if not target: miss.append(key); continue
        f,p=target
        p["coordinates"]={"lat":la,"lon":lo}
        m=p.get("maps") or {}
        if isinstance(m.get("yandex"),str) and "&ll=" in m["yandex"]:
            m["yandex"]=m["yandex"].split("&ll=")[0]+f"&ll={lo},{la}&z=17"
        updated.add(f); done+=1
        print(f"  ✓ {p['slug']:32s} -> {la},{lo}")
    for f in updated:
        json.dump(files[f],open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print(f"\nĐã cập nhật {done} điểm.", ("Không tìm thấy: "+", ".join(miss)) if miss else "")
    if done:
        print("Đang build lại...")
        os.system(f'cd "{ROOT}" && "{sys.executable}" tools/build.py')

if __name__=="__main__": main()
