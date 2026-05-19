class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, pelanggan):
        if self.is_full():
            print("Antrean penuh")
            return

        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN

        self.q[self.rear_idx] = pelanggan
        print(f"Pelanggan '{pelanggan}' berhasil masuk ke antrean.")

    def dequeue(self):
        if self.is_empty():
            print("Antrean kosong, tidak ada pelanggan yang dilayani.")
            return

        print(f"Pelanggan '{self.q[self.front_idx]}' sedang dilayani.")

        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Antrean kosong.")
            return

        print(f"Pelanggan paling depan: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("Antrean pelanggan kosong.")
            return

        print("Daftar antrean pelanggan:")
        i = self.front_idx
        nomor = 1

        while True:
            print(f"{nomor}. {self.q[i]}")

            if i == self.rear_idx:
                break

            i = (i + 1) % self.MAXN
            nomor += 1


def main():
    queue = QueueArray()
    pilih = 0

    while pilih != 5:
        print("\n=== QUEUE ARRAY ANTREAN PELANGGAN ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Pelanggan Terdepan")
        print("4. Tampilkan Antrean")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            nama = input("Masukkan nama pelanggan: ")
            queue.enqueue(nama)

        elif pilih == 2:
            queue.dequeue()

        elif pilih == 3:
            queue.peek()

        elif pilih == 4:
            queue.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()