"""
NAMA    : ALFIYAN NAZAR
KELAS   : TI22K
NIM     : 220511053

"""
import tkinter as tk
import math

def hitung_luas_volume():
    try:
        # Ambil jari-jari dari input pengguna
        jari_jari = float(jari_jari_entry.get())
        
        # Hitung luas dan volume bola
        luas = 4 * math.pi * jari_jari ** 2
        volume = (4/3) * math.pi * jari_jari ** 3
        
        # Update label hasil
        luas_var.set(f"Luas Bola: {luas:.2f}")
        volume_var.set(f"Volume Bola: {volume:.2f}")
    except ValueError:
        luas_var.set("Masukkan angka valid")
        volume_var.set("Masukkan angka valid")

# Membuat jendela tkinter
window = tk.Tk()
window.title("Menghitung Luas dan Volume Bola")

# Frame utama
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Label jari-jari
jari_jari_label = tk.Label(frame, text="Jari-Jari Bola:")
jari_jari_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Input jari-jari
jari_jari_entry = tk.Entry(frame)
jari_jari_entry.grid(row=0, column=1, padx=10, pady=10)

# Tombol hitung
hitung_button = tk.Button(frame, text="Hitung", command=hitung_luas_volume)
hitung_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# Hasil luas dan volume
luas_var = tk.StringVar()
luas_label = tk.Label(frame, textvariable=luas_var)
luas_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="w")

volume_var = tk.StringVar()
volume_label = tk.Label(frame, textvariable=volume_var)
volume_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")

window.mainloop()
