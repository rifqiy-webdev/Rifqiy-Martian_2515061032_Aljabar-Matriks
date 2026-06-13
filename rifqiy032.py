def buat_matriks(data):
    if not data:
        print("Matriks tidak boleh kosong")
        return None

    jumlah_kolom = len(data[0]) 
    
    for baris in data:
        if len(baris) != jumlah_kolom:
            print("Jumlah kolom setiap baris harus sama")
            return None

    return data


def tampilkan_matriks(m):
    for baris in m:
        print(baris)

def perkalian_matriks(A, B):
    if len(A[0]) != len(B):
        print("Perkalian matriks tidak dapat dilakukan")
        return None

    hasil = []

    for i in range(len(A)):
        baris = []

        for j in range(len(B[0])):
            jumlah = 0

            for k in range(len(B)):
                jumlah += A[i][k] * B[k][j]

            baris.append(jumlah)

        hasil.append(baris)

    return hasil

def transpose_matriks(A):
    hasil = []

    for j in range(len(A[0])):
        baris = []

        for i in range(len(A)):
            baris.append(A[i][j])

        hasil.append(baris)

    return hasil


def determinan_2x2(A):
    return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])


def invers_matriks_2x2(A):
    det = determinan_2x2(A)

    if det == 0:
        print("Matriks tidak memiliki invers")
        return None

    return [
        [A[1][1] / det, -A[0][1] / det],
        [-A[1][0] / det, A[0][0] / det]
    ]


def determinan_3x3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def invers_matriks_3x3(A):
    det = determinan_3x3(A)

    if det == 0:
        print("Matriks tidak memiliki invers")
        return None

    adj = [
        [
            (A[1][1] * A[2][2] - A[1][2] * A[2][1]),
            -(A[0][1] * A[2][2] - A[0][2] * A[2][1]),
            (A[0][1] * A[1][2] - A[0][2] * A[1][1])
        ],
        [
            -(A[1][0] * A[2][2] - A[1][2] * A[2][0]),
            (A[0][0] * A[2][2] - A[0][2] * A[2][0]),
            -(A[0][0] * A[1][2] - A[0][2] * A[1][0])
        ],
        [
            (A[1][0] * A[2][1] - A[1][1] * A[2][0]),
            -(A[0][0] * A[2][1] - A[0][1] * A[2][0]),
            (A[0][0] * A[1][1] - A[0][1] * A[1][0])
        ]
    ]

    hasil = []

    for i in range(3):
        baris = []

        for j in range(3):
            baris.append(adj[i][j] / det)

        hasil.append(baris)

    return hasil