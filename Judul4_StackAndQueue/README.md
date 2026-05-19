## PROGRAM ANTRIAN PELANGGAN
## A. Judul Program
Antrian pelanggan dengan menggunakan queue array
## B. Deskripsi Singkat
Program ini merupakan implementasi Queue menggunakan Array. Studi kasus yang digunakan dalam program ini adalah antrean pelanggan, misalnya antrean di kasir, loket pelayanan, restoran, laundry, atau tempat layanan lainnya. Queue adalah struktur data yang bekerja dengan prinsip FIFO (First In First Out), yaitu data yang pertama masuk akan menjadi data pertama yang keluar. Dalam studi kasus ini, pelanggan yang datang terlebih dahulu akan masuk ke antrean paling depan dan akan dilayani terlebih dahulu.
## C. Source Code
Screenshot Source Code di bawah ini:
<img width="1913" height="950" alt="Screenshot 2026-05-19 213053" src="https://github.com/user-attachments/assets/97c654cc-0b1e-449d-99e4-3daa175fb6b8" />
<img width="1845" height="498" alt="Screenshot 2026-05-19 213126" src="https://github.com/user-attachments/assets/d6657652-a9d7-4238-a4c1-c3bd8e69e8bb" />
<img width="1866" height="811" alt="Screenshot 2026-05-19 213216" src="https://github.com/user-attachments/assets/63f44189-f418-41a1-a6e7-0fa4bd27ab34" />
Penjelasan code:

Pada bagian awal terdapat class:
   
    class QueueArray:
Class ini digunakan untuk membuat struktur antrean pelanggan.


Di dalamnya ada fungsi __init__():
    
    def __init__(self, max_size=100):
    self.MAXN = max_size
    self.q = [None] * self.MAXN
    self.front_idx = -1
    self.rear_idx = -1
    
Bagian ini berfungsi untuk menyiapkan antrean. MAXN adalah kapasitas maksimal antrean. q adalah array/list untuk menyimpan nama pelanggan. front_idx digunakan untuk menunjuk pelanggan paling depan, sedangkan rear_idx menunjuk pelanggan paling belakang. Nilai awalnya -1 karena antrean masih kosong.

Fungsi berikutnya adalah:
   
    def is_empty(self):
    return self.front_idx == -1
    
Fungsi ini digunakan untuk mengecek apakah antrean kosong. Jika front_idx bernilai -1, berarti belum ada pelanggan dalam antrean.

Lalu ada fungsi:
    
    def is_full(self):
      return (self.rear_idx + 1) % self.MAXN == self.front_idx
      
Fungsi ini digunakan untuk mengecek apakah antrean sudah penuh. Program ini memakai konsep circular queue, jadi posisi belakang antrean bisa kembali ke awal array jika sudah mencapai batas akhir.

Fungsi enqueue():
    
    def enqueue(self, pelanggan):
    
Fungsi ini digunakan untuk menambahkan pelanggan ke antrean. Jika antrean penuh, program akan menampilkan pesan “Antrean penuh”. Jika antrean kosong, maka front_idx dan rear_idx diatur ke posisi 0. Jika antrean sudah berisi data, maka rear_idx akan maju ke posisi berikutnya, lalu nama pelanggan dimasukkan ke dalam array.

Fungsi dequeue():
    
    def dequeue(self):
    
Fungsi ini digunakan untuk melayani pelanggan yang berada di posisi paling depan. Jika antrean kosong, program akan memberi pesan bahwa tidak ada pelanggan yang dilayani. Jika ada pelanggan, maka pelanggan pada posisi front_idx akan diproses. Setelah itu, front_idx bergeser ke pelanggan berikutnya.

Fungsi peek():
   
    def peek(self):
    
Fungsi ini digunakan untuk melihat pelanggan yang berada di posisi paling depan tanpa menghapusnya dari antrean. Jadi fungsi ini hanya menampilkan pelanggan berikutnya yang akan dilayani.

Fungsi display():
    
    def display(self):
    
Fungsi ini digunakan untuk menampilkan seluruh daftar pelanggan yang sedang mengantre, mulai dari pelanggan paling depan sampai pelanggan paling belakang.

Pada bagian main():
    
    def main():
      queue = QueueArray()
      
Program membuat objek queue dari class QueueArray. Setelah itu, program menampilkan menu secara berulang.

## D. Output Program
Screenshoot output:
<img width="1917" height="993" alt="Screenshot 2026-05-19 215113" src="https://github.com/user-attachments/assets/fa8728ee-cee9-49d5-9783-0e2a9063e7cb" />
<img width="1919" height="807" alt="Screenshot 2026-05-19 215126" src="https://github.com/user-attachments/assets/001d89ca-d08b-4c85-b78d-e6bc6989509a" />

Penjelasan output:

- Pelanggan pertama yang dimasukkan adalah Rahma.
  
- Setelah itu, pelanggan kedua yang dimasukkan adalah Eci.

- Kemudian pelanggan ketiga yang dimasukkan adalah Kei.

- Jadi, urutan antrean awal adalah Rahma, Eci, Kei.

- Pengguna memilih menu 2. Layani Pelanggan.

- Program melayani pelanggan yang berada di posisi paling depan.

- Pelanggan yang dilayani pertama adalah Rahma, karena Rahma masuk antrean lebih dulu.

- Setelah Rahma dilayani, Rahma keluar dari antrean.

- Sisa antrean setelah Rahma dilayani adalah Eci dan Kei.

- Pengguna memilih menu 3. Lihat Pelanggan Terdepan.

- Program menampilkan pelanggan paling depan, yaitu Eci.

- Hal ini terjadi karena Rahma sudah keluar dari antrean setelah dilayani.

- Pengguna memilih menu 4. Tampilkan Antrean.

- Program menampilkan daftar antrean yang tersisa, yaitu Eci di urutan pertama dan Kei di urutan kedua.

- Pengguna memilih menu 5. Keluar.

- Program berhenti dan menampilkan pesan “Program selesai.”

- Hasil akhir: program berhasil menerapkan konsep Queue Array, karena pelanggan yang masuk pertama, yaitu Rahma, dilayani terlebih dahulu.

## LINK YOUTUBE
https://youtu.be/cfRcaFfGwIg
