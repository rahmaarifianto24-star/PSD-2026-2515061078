## PROGRAM PENYIMPANAN NOMOR TIKET PELANGGAN

## A. Judul Program

Sistem penyimpanan nomor tiket pelanggan dengan menggunakan binary search tree 

## B. Deskripsi Singkat

Program ini digunakan untuk mengelola nomor tiket pelanggan pada suatu sistem pelayanan, seperti tempat servis elektronik, klinik, atau loket antrean. Setiap nomor tiket pelanggan akan disimpan ke dalam struktur binary search tree. Data yang lebih kecil akan ditempatkan di sebelah kiri, sedangkan data yang lebih besar akan ditempatkan di sebelah kanan.

## C. Source Code

Screenshot Source Code di bawah ini:
<img width="1916" height="993" alt="Screenshot 2026-05-26 172617" src="https://github.com/user-attachments/assets/16300218-ba60-49d6-bb54-d13ff985bc9c" />
<img width="1919" height="995" alt="Screenshot 2026-05-26 172634" src="https://github.com/user-attachments/assets/b1fade1c-6187-4935-8967-eb42e8721afa" />
<img width="1436" height="420" alt="Screenshot 2026-05-26 172655" src="https://github.com/user-attachments/assets/2f0b1ae8-4048-4eb8-87ba-ed5675f9ee03" />

Penjelasan: 

Class Node digunakan untuk membuat simpul pada tree. Setiap node menyimpan nomor_tiket, serta memiliki cabang left dan right.

Class BSTTiket digunakan untuk mengatur proses BST. 

Di dalamnya terdapat beberapa fungsi utama, yaitu 

      insert() 

untuk pemanggil utama untuk memasukkan nomor tiket. Method ini memanggil insert_node mulai dari root. 

      search() 

untuk memanggil proses pencarian dari root. Hasilnya berupa True jika data ditemukan dan False jika data tidak ditemukan. 

      inorder() 

untuk menampilkan semua nomor tiket secara urut dari kecil ke besar. Traversal inorder bekerja dengan urutan: cabang kiri, root, lalu cabang kanan.

      main 
      
Fungsi main adalah bagian utama program. Di dalamnya dibuat objek bst dari class BSTTiket. Objek ini digunakan untuk menjalankan fitur tambah tiket, cari tiket, dan tampilkan tiket.
## D. Output Program

Screenshoot output:

<img width="1856" height="911" alt="Screenshot 2026-05-26 184903" src="https://github.com/user-attachments/assets/63940fa5-13e5-4bd8-ba45-33b0e19fe13e" />
<img width="1851" height="463" alt="Screenshot 2026-05-26 184913" src="https://github.com/user-attachments/assets/7a20ffb5-1cac-4be9-b6de-add9d6205276" />

Penjelasan output:

- Program menampilkan menu Sistem Nomor Tiket Pelanggan.

- Pengguna memilih menu 1 untuk menambahkan nomor tiket.

- Nomor tiket yang dimasukkan adalah 12, 25, dan 78.

- Program menampilkan pesan bahwa setiap nomor tiket berhasil ditambahkan.

- Pengguna memilih menu 3 untuk menampilkan semua tiket secara terurut.

- Program menampilkan hasil: 12 25 78

- Pengguna memilih menu 2 untuk mencari nomor tiket.

- Nomor tiket yang dicari adalah 25.

- Program menampilkan bahwa nomor tiket 25 ditemukan.

- Pengguna memilih menu 4 untuk keluar, lalu program selesai.
## LINK YOUTUBE
https://youtu.be/4s1nMYDu4wY
