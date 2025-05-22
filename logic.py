from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import io
from rembg import remove
from utils import kaydet_json_ve_dosyaya

def islem_gorsel_sec(image_label):
    # Dosya sec
    yol = filedialog.askopenfilename(filetypes=[("Görseller", "*.png *.jpg *.jpeg")])
    if yol:
        # Görseli aç ve arayüzde göster
        image = Image.open(yol).convert("RGBA")
        thumb = image.copy()
        thumb.thumbnail((300, 300))
        img = ImageTk.PhotoImage(thumb)
        image_label.config(image=img)
        image_label.image = img
        return image
    return None

def islem_arka_plani_kaldir(original_image, image_label):
    if original_image:
        # Görseli byte'a çevir
        buffer = io.BytesIO()
        original_image.save(buffer, format="PNG")
        sonuc_bytes = remove(buffer.getvalue())

        # Çıkan sonucu görsele dönüştür
        result_image = Image.open(io.BytesIO(sonuc_bytes)).convert("RGBA")

        # Ön izleme için thumbnail
        thumb = result_image.copy()
        thumb.thumbnail((300, 300))
        img = ImageTk.PhotoImage(thumb)
        image_label.config(image=img)
        image_label.image = img

        messagebox.showinfo("Başarılı", "Arka plan kaldırıldı!")
        return result_image
    return None

def islem_kaydet(output_image, dosya_adi):
    from utils import kaydet_json_ve_dosyaya
    kaydet_json_ve_dosyaya(output_image, dosya_adi)

