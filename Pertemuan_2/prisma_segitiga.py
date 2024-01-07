print("\nPROGRAM MENGHITUNG LUAS DAN VOLUME PRISMA SEGITIGA\n")
'''
Programmer  : Alfiyan Nazar (220511053)
Pertemuan   : 1
Tanggal     : 22 Oktober 2023
'''

'''
Keterangan : 
S = Sisi
T = Tingi prisma
a = Alas
t = Tinggi
'''
# Nilai 
S1 = 8
S2 = 9
S3 = 10
T = 15
a = 14
t = 11
print("Nilai S1 = ", S1)
print("Nilai S2 = ", S2)
print("Nilai S3 = ", S3)
print("Nilai T  = ", T)
print("Nilai a  = ", a)
print("Nilai t  = ", t)
print(" ")

# Rumus
keliling_segitiga = S1 + S2 + S3 
luas_segitiga = keliling_segitiga * T
luas_prisma = keliling_segitiga * T + a * t
volume = 1/2 * a * t * T

# Hasil
print("Keliling Segitiga      = ", keliling_segitiga)
print("Luas Segitiga          = ", luas_segitiga)
print("Luas Prisma Segitiga   = ", luas_prisma)
print("Volume Prisma Segitiga = ", volume)
