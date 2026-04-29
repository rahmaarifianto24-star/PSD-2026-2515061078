class Node:
    def __init__(self, lagu):
        self.lagu = lagu
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    # tambah lagu
    def tambah(self, lagu):
        new_node = Node(lagu)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print("Lagu ditambahkan!")

    # tampilkan playlist
    def tampil(self):
        if self.head is None:
            print("Playlist kosong")
        else:
            temp = self.head
            print("\nPlaylist:")
            while temp:
                print("-", temp.lagu)
                temp = temp.next

    # putar lagu pertama
    def putar(self):
        if self.head is None:
            print("Tidak ada lagu")
        else:
            print("Memutar:", self.head.lagu)

    # hapus lagu berdasarkan judul
    def hapus(self, lagu):
        temp = self.head
        prev = None

        while temp:
            if temp.lagu.lower() == lagu.lower():
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                print("Lagu dihapus!")
                return
            prev = temp
            temp = temp.next

        print("Lagu tidak ditemukan")


# program utama
pl = Playlist()

while True:
    print("\n=== MENU PLAYLIST ===")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Putar Lagu")
    print("4. Hapus Lagu")
    print("5. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        lagu = input("Masukkan judul lagu: ")
        pl.tambah(lagu)

    elif pilih == "2":
        pl.tampil()

    elif pilih == "3":
        pl.putar()

    elif pilih == "4":
        lagu = input("Masukkan lagu yang dihapus: ")
        pl.hapus(lagu)

    elif pilih == "5":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")
