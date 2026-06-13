import rifqiy032

A = rifqiy032.buat_matriks([[1, 2, 1], [3, 4, 2],[5, 6, 3]])
print("\nMatriks A:")
rifqiy032.tampilkan_matriks(A)

B = rifqiy032.buat_matriks([[5, 6, 7], [8, 9, 10], [11, 12, 13]])
print("\nMatriks B:")
rifqiy032.tampilkan_matriks(B)

hasil_kali = rifqiy032.perkalian_matriks(A, B)
print("\nHasil Perkalian A × B:")
rifqiy032.tampilkan_matriks(hasil_kali)

hasil_transpose_A = rifqiy032.transpose_matriks(A)
print("\nTranspose A:")
rifqiy032.tampilkan_matriks(hasil_transpose_A)

C = rifqiy032.buat_matriks([[1, 2, 3], [0, 1, 4], [5, 6, 0]])

detC = rifqiy032.determinan_3x3(C)
print("\nDeterminan C  =", detC)

invC = rifqiy032.invers_matriks_3x3(C)
print("\nInvers C (3x3):")
rifqiy032.tampilkan_matriks(invC)

hasil_identitas =  rifqiy032.perkalian_matriks(C, invC)
print("\nC × C⁻¹:")
rifqiy032.tampilkan_matriks(hasil_identitas)