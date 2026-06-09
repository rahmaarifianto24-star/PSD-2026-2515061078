## PROGRAM BUKU KONTAK
## A. Judul Program

Pendataan kontak telepon menggunakan hash map

## B. Deskripsi Singkat
Hash Map Buku Kontak adalah program sederhana yang digunakan untuk menyimpan dan mengelola data kontak telepon menggunakan struktur data Hash Map. Program ini memungkinkan pengguna untuk menambah, mencari, menghapus, dan menampilkan kontak dengan cepat berdasarkan nama. Dalam program ini, nama kontak berfungsi sebagai key dan nomor telepon sebagai value, sehingga proses pencarian data dapat dilakukan secara efisien.
## Source Code
Screenshot Source Code di bawah ini:
<img width="1911" height="961" alt="Screenshot 2026-06-09 194639" src="https://github.com/user-attachments/assets/cbffe68d-e053-46b4-b760-61861735f5c6" />
<img width="1917" height="952" alt="Screenshot 2026-06-09 194700" src="https://github.com/user-attachments/assets/dfa92174-9170-48fc-a6fe-36fe8c9e5987" />
Penjelasan code:
1. Class HashMapKontak
   Class HashMapKontak digunakan untuk menyimpan dan mengelola data kontak telepon menggunakan struktur data Hash Map.
Atribut yang digunakan:
- kontak → menyimpan data kontak dalam bentuk pasangan nama dan nomor telepon.
Setiap data disimpan dengan format:
- Key → Nama kontak
- Value → Nomor telepon

a. Method __init__

Digunakan untuk menginisialisasi Hash Map dengan kondisi awal kosong.
Variabel kontak diisi dengan {} yang berarti belum ada data kontak yang tersimpan.

b. Method tambah_kontak(nama, nomor)
Digunakan untuk menambahkan kontak baru ke dalam Hash Map dengan nama sebagai key dan nomor telepon sebagai value.

c. Method cari_kontak(nama)
Digunakan untuk mencari nomor telepon berdasarkan nama kontak.

d. Method hapus_kontak(nama)
Digunakan untuk menghapus kontak berdasarkan nama yang diinput.

e. Method tampilkan_kontak(nama)
Digunakan untuk menampilkan seluruh kontak yang tersimpan dalam Hash Map.

2. Program Utama
   Program dimulai dengan membuat objek dari class HashMapKontak:

        buku_kontak = HashMapKontak()

## D. Output Program
Screenshoot output:
<img width="1912" height="762" alt="Screenshot 2026-06-09 204607" src="https://github.com/user-attachments/assets/82da63f4-2815-4092-badc-782a2b62e2de" />
<img width="1919" height="763" alt="Screenshot 2026-06-09 204619" src="https://github.com/user-attachments/assets/9eccde60-2eaf-40c5-8591-c1bc25927d72" />
<img width="1901" height="738" alt="Screenshot 2026-06-09 204629" src="https://github.com/user-attachments/assets/d96cc3fc-6b4c-436a-b0ec-8ee80f8d0c8b" />

Penjelasan output:
**Penjelasan Output:**

- Kontak pertama yang dimasukkan adalah Rahma dengan nomor telepon 08314171031691.
- Kontak kedua yang dimasukkan adalah Eci dengan nomor telepon 083631793018.
- Kontak ketiga yang dimasukkan adalah Kei dengan nomor telepon 08216314718.
- Pengguna memilih menu 4. Tampilkan Semua Kontak.
- Program menampilkan seluruh kontak yang tersimpan, yaitu Rahma, Eci, dan Kei beserta nomor telepon masing-masing.
- Selanjutnya pengguna memilih menu 2. Cari Kontak.
- Program mencari kontak dengan nama Eci dan berhasil menemukan nomor telepon 083631793018.
- Setelah itu pengguna memilih menu 3. Hapus Kontak.
- Program menghapus kontak Rahma dari Hash Map karena nama tersebut ditemukan dalam daftar kontak.
- Kemudian pengguna kembali memilih menu 4. Tampilkan Semua Kontak.
- Program menampilkan kontak yang tersisa, yaitu Eci dan Kei. Kontak Rahma sudah tidak muncul karena telah dihapus.
- Terakhir, pengguna memilih menu 5. Keluar.
- Program berhenti dan menampilkan pesan "Program selesai."

Hasil akhir: program berhasil menerapkan konsep Hash Map, karena data kontak dapat ditambahkan, dicari, ditampilkan, dan dihapus dengan cepat menggunakan nama kontak sebagai key dan nomor telepon sebagai value.

## LINK YOUTUBE
https://youtu.be/cXkCFJfHEQs
