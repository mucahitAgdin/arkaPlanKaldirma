import os
import json
from datetime import datetime
from PIL import Image

def kaydet_json_ve_dosyaya(image, dosya_adi, klasor='kayitlar', json_dosya='veritabani.json'):
    # Klasör yoksa oluştur
    os.makedirs(klasor, exist_ok=True)

    # Uygun uzantıyı kontrol et (.png yoksa ekle)
    if not dosya_adi.lower().endswith('.png'):
        dosya_adi += '.png'

    # Tam dosya yolu oluştur
    tam_yol = os.path.join(klasor, dosya_adi)

    # Görseli kaydet
    image.save(tam_yol)

    # JSON kaydı oluştur
    kayit = {
        "id": os.path.splitext(dosya_adi)[0],  # uzantısız hali
        "filename": dosya_adi,
        "kayit_zamani": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    # JSON dosyasını yükle (varsa)
    if os.path.exists(json_dosya):
        with open(json_dosya, "r", encoding="utf-8") as f:
            try:
                veriler = json.load(f)
            except json.JSONDecodeError:
                veriler = []
    else:
        veriler = []

    # Yeni kayıt ekle ve yaz
    veriler.append(kayit)
    with open(json_dosya, "w", encoding="utf-8") as f:
        json.dump(veriler, f, indent=2)
