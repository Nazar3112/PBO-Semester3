"""
NAMA    : ALFIYAN NAZAR
KELAS   : TI22K
NIM     : 220511053

"""
import tkinter as tk

def hitung_luas_volume():
    try:
        # Ambil panjang, lebar, dan tinggi dari input pengguna
        panjang = float(panjang_entry.get())
        lebar = float(lebar_entry.get())
        tinggi = float(tinggi_entry.get())
        
        # Hitung luas permukaan dan volume balok
        luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        volume = panjang * lebar * tinggi
        
        # Update label hasil
        luas_permukaan_var.set(f"Luas Permukaan Balok: {luas_permukaan:.2f}")
        volume_var.set(f"Volume Balok: {volume:.2f}")
    except ValueError:
        luas_permukaan_var.set("Masukkan angka valid")
        volume_var.set("Masukkan angka valid")

# Membuat jendela tkinter
window = tk.Tk()
window.title("Menghitung Luas Permukaan dan Volume Balok")

# Frame utama
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Label panjang, lebar, dan tinggi
panjang_label = tk.Label(frame, text="Panjang Balok:")
panjang_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

lebar_label = tk.Label(frame, text="Lebar Balok:")
lebar_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

tinggi_label = tk.Label(frame, text="Tinggi Balok:")
tinggi_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Input panjang, lebar, dan tinggi
panjang_entry = tk.Entry(frame)
panjang_entry.grid(row=0, column=1, padx=10, pady=10)

lebar_entry = tk.Entry(frame)
lebar_entry.grid(row=1, column=1, padx=10, pady=10)

tinggi_entry = tk.Entry(frame)
tinggi_entry.grid(row=2, column=1, padx=10, pady=10)

# Tombol hitung
hitung_button = tk.Button(frame, text="Hitung", command=hitung_luas_volume)
hitung_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# Hasil luas permukaan dan volume
luas_permukaan_var = tk.StringVar()
luas_permukaan_label = tk.Label(frame, textvariable=luas_permukaan_var)
luas_permukaan_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")

volume_var = tk.StringVar()
volume_label = tk.Label(frame, textvariable=volume_var)
volume_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")

window.mainloop()
