"""
NAMA    : ALFIYAN NAZAR
KELAS   : TI22K
NIM     : 220511053

"""
import tkinter as tk
import math

def hitung_luas_volume():
    try:
        # Ambil jari-jari dan tinggi kerucut dari input pengguna
        jari_jari = float(jari_jari_entry.get())
        tinggi = float(tinggi_entry.get())
        
        # Hitung luas permukaan dan volume kerucut
        luas_permukaan = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari**2 + tinggi**2))
        volume = (1/3) * math.pi * jari_jari**2 * tinggi
        
        # Update label hasil
        luas_permukaan_var.set(f"Luas Permukaan Kerucut: {luas_permukaan:.2f}")
        volume_var.set(f"Volume Kerucut: {volume:.2f}")
    except ValueError:
        luas_permukaan_var.set("Masukkan angka valid")
        volume_var.set("Masukkan angka valid")

# Membuat jendela tkinter
window = tk.Tk()
window.title("Menghitung Luas Permukaan dan Volume Kerucut")

# Frame utama
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Label jari-jari dan tinggi
jari_jari_label = tk.Label(frame, text="Jari-Jari Kerucut:")
jari_jari_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

tinggi_label = tk.Label(frame, text="Tinggi Kerucut:")
tinggi_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Input jari-jari dan tinggi
jari_jari_entry = tk.Entry(frame)
jari_jari_entry.grid(row=0, column=1, padx=10, pady=10)

tinggi_entry = tk.Entry(frame)
tinggi_entry.grid(row=1, column=1, padx=10, pady=10)

# Tombol hitung
hitung_button = tk.Button(frame, text="Hitung", command=hitung_luas_volume)
hitung_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# Hasil luas permukaan dan volume
luas_permukaan_var = tk.StringVar()
luas_permukaan_label = tk.Label(frame, textvariable=luas_permukaan_var)
luas_permukaan_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")

volume_var = tk.StringVar()
volume_label = tk.Label(frame, textvariable=volume_var)
volume_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")

window.mainloop()
