class HashMapKontak:
    def __init__(self):
        self.kontak = {}

    def tambah_kontak(self, nama, nomor):
        self.kontak[nama] = nomor
        print(f"Kontak {nama} berhasil ditambahkan.")

    def cari_kontak(self, nama):
        if nama in self.kontak:
            print(f"Nomor {nama}: {self.kontak[nama]}")
        else:
            print("Kontak tidak ditemukan.")

    def hapus_kontak(self, nama):
        if nama in self.kontak:
            del self.kontak[nama]
            print(f"Kontak {nama} berhasil dihapus.")
        else:
            print("Kontak tidak ditemukan.")

    def tampilkan_kontak(self):
        if not self.kontak:
            print("Daftar kontak kosong.")
        else:
            print("\nDaftar Kontak:")
            for nama, nomor in self.kontak.items():
                print(f"{nama} : {nomor}")


def main():
    buku_kontak = HashMapKontak()

    while True:
        print("\n=== BUKU KONTAK ===")
        print("1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Hapus Kontak")
        print("4. Tampilkan Semua Kontak")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nomor = input("Masukkan nomor telepon: ")
            buku_kontak.tambah_kontak(nama, nomor)

        elif pilihan == "2":
            nama = input("Masukkan nama yang dicari: ")
            buku_kontak.cari_kontak(nama)

        elif pilihan == "3":
            nama = input("Masukkan nama yang akan dihapus: ")
            buku_kontak.hapus_kontak(nama)

        elif pilihan == "4":
            buku_kontak.tampilkan_kontak()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()