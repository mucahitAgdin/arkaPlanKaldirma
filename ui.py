import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk
from logic import islem_gorsel_sec, islem_arka_plani_kaldir, islem_kaydet

class ArkaPlanKaldirmaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🖼️ Arka Plan Kaldırıcı")
        self.root.geometry("800x600")
        self.root.config(bg="#f0f0f0")

        # Görselin gösterileceği alan
        self.image_label = tk.Label(root, text="Henüz görsel seçilmedi.", bg="#f0f0f0", font=("Arial", 12))
        self.image_label.pack(pady=20)

        # Butonlar
        self.sec_buton = tk.Button(root, text="📂 Görsel Seç", command=self.gorsel_sec, width=20, bg="#d1e7dd", font=("Arial", 11))
        self.sec_buton.pack(pady=10)

        self.kaldir_buton = tk.Button(root, text="🧼 Arka Planı Kaldır", command=self.arka_plani_kaldir, width=20, state="disabled", bg="#ffeeba", font=("Arial", 11))
        self.kaldir_buton.pack(pady=10)

        self.kaydet_buton = tk.Button(root, text="💾 Kaydet (JSON)", command=self.kaydet, width=20, state="disabled", bg="#cfe2ff", font=("Arial", 11))
        self.kaydet_buton.pack(pady=10)

        # Görsel verisi
        self.original_image = None
        self.output_image = None

    def gorsel_sec(self):
        self.original_image = islem_gorsel_sec(self.image_label)
        if self.original_image:
            self.kaldir_buton.config(state="normal")

    def arka_plani_kaldir(self):
        self.output_image = islem_arka_plani_kaldir(self.original_image, self.image_label)
        if self.output_image:
            self.kaydet_buton.config(state="normal")

    def kaydet(self):
        if self.output_image:
            islem_kaydet(self.output_image)
