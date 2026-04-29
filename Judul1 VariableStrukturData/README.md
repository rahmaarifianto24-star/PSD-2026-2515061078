SISTEM PLAYLIST LAGU (LINKED LIST)

A. Judul Program

Sistem Playlist Lagu Menggunakan Linked List

B. Deskripsi Singkat

Program ini merupakan implementasi struktur data Linked List (Single Linked List) menggunakan bahasa Python. 
Program digunakan untuk mengelola playlist lagu secara sederhana, di mana setiap lagu disimpan dalam node yang saling terhubung. Linked List dipilih karena memungkinkan penambahan dan penghapusan data secara fleksibel tanpa perlu menggeser elemen seperti pada array. 

C. Source Code 

Screenshot Source Code
Tambahkan gambar source code di bawah ini:  
<img width="1465" height="822" alt="Screenshot 2026-04-29 180754" src="https://github.com/user-attachments/assets/80a74171-8ad4-47f6-b4a8-c3ef908e5e1f" />
<img width="1458" height="633" alt="Screenshot 2026-04-29 180813" src="https://github.com/user-attachments/assets/7ff562b9-96c6-42b6-8f76-cf3bebd225bd" />
<img width="1472" height="834" alt="Screenshot 2026-04-29 180838" src="https://github.com/user-attachments/assets/2b8396ad-7028-4a64-97bb-2d047eb4d828" />

Penjelasan code 
1. Class Node

Class Node digunakan sebagai tempat untuk menyimpan satu data lagu dalam playlist.

Di dalamnya terdapat dua atribut:

      lagu → berisi judul lagu
      next → sebagai penghubung ke lagu berikutnya

Setiap node akan saling terhubung, sehingga membentuk rangkaian seperti rantai (Linked List).


2. Class Playlist

  berfungsi untuk mengelola seluruh data lagu yang tersimpan dalam Linked List.

a. Method __init__()

  digunakan untuk menginisialisasi Linked List dengan kondisi awal kosong.

Variabel head di-set ke None, yang berarti belum ada lagu dalam playlist.


b. Method tambah(lagu)

digunakan untuk menambahkan lagu baru ke dalam playlist.



- Membuat node baru dari input lagu

- Jika playlist masih kosong → lagu langsung menjadi head

- Jika sudah ada isi → program mencari node terakhir lalu menambahkan lagu di bagian akhir


c. Method tampil()

digunakan untuk menampilkan seluruh lagu dalam playlist.


- Dimulai dari head

- Menggunakan perulangan untuk menelusuri setiap node

- Setiap lagu akan ditampilkan satu per satu sesuai urutan
    

d. Method putar()

digunakan untuk memutar lagu pertama dalam playlist.

- Lagu yang diputar adalah data pada head

- Jika playlist kosong, maka akan muncul pesan bahwa tidak ada lagu


e. Method hapus(lagu)

digunakan untuk menghapus lagu berdasarkan judul yang diinput.



3. Program Utama

Program utama dimulai dengan membuat objek dari class Playlist:

    pl = Playlist()



4. Menu Program

Program menggunakan perulangan while True agar menu terus ditampilkan.



5. Input dan Percabangan

User memasukkan pilihan, kemudian program menjalankan fungsi sesuai menu menggunakan if-elif.

D. Output Program
Screenshoot program
<img width="1452" height="899" alt="Screenshot 2026-04-29 181340" src="https://github.com/user-attachments/assets/462909fc-c8f1-40bc-98c3-a3bd87b02a05" />
<img width="1482" height="799" alt="Screenshot 2026-04-29 181401" src="https://github.com/user-attachments/assets/a56184e8-cbb1-4c91-82be-916d0a3bdc00" />
<img width="1508" height="632" alt="Screenshot 2026-04-29 181444" src="https://github.com/user-attachments/assets/0d57a6a9-e8bc-44df-bfa8-4a29124611ea" />

Penjelasan output

- Saat user memasukkan pilihan menu → program membaca input untuk menentukan fitur yang dijalankan

- Saat memilih menu tidak tersedia → muncul pesan "Pilihan tidak valid!"

- Saat menambah lagu → data lagu masuk ke dalam Linked List

- Saat menampilkan playlist → semua lagu ditampilkan secara berurutan dari awal sampai akhir

- Saat memutar lagu → lagu pertama (head) ditampilkan sebagai lagu yang sedang diputar

- Saat menghapus lagu → lagu yang dipilih akan dihapus dari Linked List

- Saat lagu tidak ditemukan → muncul pesan "Lagu tidak ditemukan
