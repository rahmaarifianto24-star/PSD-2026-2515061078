def binary_search(nilai_mahasiswa, target):
    kiri = 0
    kanan = len(nilai_mahasiswa) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        print(f"\nPosisi tengah : {tengah}")
        print(f"Nilai tengah  : {nilai_mahasiswa[tengah]}")

        if nilai_mahasiswa[tengah] == target:
            return tengah

        elif nilai_mahasiswa[tengah] < target:
            print("Pencarian ke kanan")
            kiri = tengah + 1

        else:
            print("Pencarian ke kiri")
            kanan = tengah - 1

    return -1

def main():

    print("--- PROGRAM BINARY SEARCH NILAI MAHASISWA ---")

    # Input jumlah mahasiswa
    while True:
        try:
            n = int(input("Masukkan jumlah mahasiswa: "))
            break
        except ValueError:
            print("Input harus angka!")

    nilai_mahasiswa = []

    print("\nMasukkan nilai mahasiswa secara urut menaik:")

    for i in range(n):
        while True:
            try:
                nilai = int(input(f"Nilai mahasiswa ke-{i+1}: "))
                nilai_mahasiswa.append(nilai)
                break
            except ValueError:
                print("Input harus angka!")

    print("\nData Nilai Mahasiswa :", nilai_mahasiswa)

    while True:
        try:
            target = int(input("\nMasukkan nilai yang ingin dicari: "))
            break
        except ValueError:
            print("Input harus angka!")

    hasil = binary_search(nilai_mahasiswa, target)

    if hasil != -1:
        print(f"\nNilai {target} ditemukan pada indeks ke-{hasil}")
    else:
        print(f"\nNilai {target} tidak ditemukan")

if __name__ == "__main__":
    main()