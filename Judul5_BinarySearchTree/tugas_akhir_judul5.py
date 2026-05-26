class Node:
    def __init__(self, nomor_tiket):
        self.nomor_tiket = nomor_tiket
        self.left = None
        self.right = None


class BSTTiket:
    def __init__(self):
        self.root = None

    def insert_node(self, root, nomor_tiket):
        if root is None:
            return Node(nomor_tiket)
        if nomor_tiket < root.nomor_tiket:
            root.left = self.insert_node(root.left, nomor_tiket)
        elif nomor_tiket > root.nomor_tiket:
            root.right = self.insert_node(root.right, nomor_tiket)
        else:
            print("Nomor tiket sudah terdaftar!")
        return root

    def insert(self, nomor_tiket):
        self.root = self.insert_node(self.root, nomor_tiket)

    def search_node(self, root, nomor_tiket):
        if root is None:
            return False
        if root.nomor_tiket == nomor_tiket:
            return True
        if nomor_tiket < root.nomor_tiket:
            return self.search_node(root.left, nomor_tiket)
        else:
            return self.search_node(root.right, nomor_tiket)

    def search(self, nomor_tiket):
        return self.search_node(self.root, nomor_tiket)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.nomor_tiket, end=" ")
            self.inorder(root.right)


def main():
    bst = BSTTiket()
    while True:
        print("\n=== SISTEM NOMOR TIKET PELANGGAN ===")
        print("1. Tambah Nomor Tiket")
        print("2. Cari Nomor Tiket")
        print("3. Tampilkan Semua Tiket Terurut")
        print("4. Keluar")

        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue
        if pilihan == 1:
            try:
                nomor = int(input("Masukkan nomor tiket pelanggan: "))
                bst.insert(nomor)
                print(f"Nomor tiket {nomor} berhasil ditambahkan.")
            except ValueError:
                print("Nomor tiket harus berupa angka!")
        elif pilihan == 2:
            try:
                nomor = int(input("Masukkan nomor tiket yang dicari: "))

                if bst.search(nomor):
                    print(f"Nomor tiket {nomor} ditemukan.")
                else:
                    print(f"Nomor tiket {nomor} tidak ditemukan.")
            except ValueError:
                print("Nomor tiket harus berupa angka!")
        elif pilihan == 3:
            print("Daftar nomor tiket terurut:", end=" ")
            bst.inorder(bst.root)
            print()
        elif pilihan == 4:
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()