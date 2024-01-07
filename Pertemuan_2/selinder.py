print("\nPROGRAM MENGHITUNG LUAS DAN VOLUME SELINDER\n")
'''
Programmer  : Alfiyan Nazar (220511053)
Pertemuan   : 1
Tanggal     : 22 Oktober 2023
'''

'''
Keterangan : 
L = Luas permukaan tabung
r = Jari - jari
T = Tinggi
phi = konstanta yang bernilai 3.14 atau 22/7
'''
# Nilai
phi = 3.14
r   = 15
T   = 46
print("Nilai phi = ", phi)
print("Nilai r = ", r)
print("Nilai T = ", T)
print(" ")

# Rumus
luas_selimut = 2 * phi * r * T
luas_permukaan = (2 * phi * r * T) + (2 * phi * r**2)
voloume = phi * r**2 * T

# Hasil
print("Luas Selimut    = ", luas_selimut)
print("Luas Permukaan  = ", luas_permukaan)
print("Volume Selinder = ", voloume)
