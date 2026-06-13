import rifqiy032
v = rifqiy032.buat_matriks([[3],[2],[2]])
print("\nuji matrisk")
rifqiy032.tampilkan_matriks(v)

# Membuat Matriks
A = rifqiy032.buat_matriks([[1, 2], [3, 4]])
print("\nMatriks A:")
rifqiy032.tampilkan_matriks(A)

# Perkalian Matriks
B = [[5, 6], [7, 8]]
print("\nMatriks B:")
rifqiy032.tampilkan_matriks(B)
hasil_kali = rifqiy032.perkalian_matriks(A, B)

print("\nHasil Perkalian A × B:")
rifqiy032.tampilkan_matriks(hasil_kali)

# Transpose Matriks
hasil_transpose = rifqiy032.transpose_matriks(A)

print("\nTranspose A:")
rifqiy032.tampilkan_matriks(hasil_transpose)

# Determinan 2x2
det2 = rifqiy032.determinan_2x2(A)
print("\nDeterminan A (2x2) =", det2)

# Invers 2x2
inv2 = rifqiy032.invers_matriks_2x2(A)

print("\nInvers A (2x2):")
rifqiy032.tampilkan_matriks(inv2)

# Determinan 3x3
C = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]

det3 = rifqiy032.determinan_3x3(C)
print("\nDeterminan C (3x3) =", det3)

# Invers 3x3
inv3 = rifqiy032.invers_matriks_3x3(C)

print("\nInvers C (3x3):")
rifqiy032.tampilkan_matriks(inv3)

# Perkalian Matriks dengan Inversnya
hasil_identitas =  rifqiy032.perkalian_matriks(A, inv2)

print("\nA × A⁻¹:")
rifqiy032.tampilkan_matriks(hasil_identitas)