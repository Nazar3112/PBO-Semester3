print("\nPROGRAM MENGHITUNG LUAS DAN VOLUME KERUCUT\n")
'''
Programmer  : Alfiyan Nazar (220511053)
Pertemuan   : 1
Tanggal     : 22 Oktober 2023
'''

'''
Keterangan : 
L   = luas permukaan kerucut
r   = jari - jari
T   = tinggi
s   = garis pelukis
phi = konstanta yang bernilai 3.14 atau 22/7
'''

# Nilai
phi = 3.14
r = 4
s = 7
T = 10

print("Nilai Phi = ", phi)
print("Nilai r   = ", r)
print("Nilai s   = ", s)
print("Nilai T   = ", T)
print(" ")


# Rumus
Luas_selimut = phi * r * s
Luas_permukaan = (phi * r * s) + (phi * r**2)
Volume = 1/3 * phi * r**2 * T

# Hasil
print("Luas Selimut   = ", Luas_selimut)
print("Luas Permukaan = ", Luas_permukaan)
print("Volume Kerucut =", Volume)
