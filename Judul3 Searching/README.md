## PROGRAM MENCARI NILAI MAHASISWA
## A. Judul Program
Mencari nilai mahasiswa dengan menggunakan binary search
## B. Deskripsi Singkat 
Program untuk mencari nilai mahasiswa dengan menggunakan metode Binary Search dalam bahasa Python. Program meminta pengguna untuk memasukkan data nilai mahasiswa yang sudah diurutkan, lalu mencari nilai tertentu dengan cara membandingkan nilai di tengah data secara terus-menerus hingga nilai tersebut ditemukan atau tidak ditemukan. Metode ini membuat proses pencarian menjadi lebih cepat dan efisien.
## C. Source Code
Screenshot Source Code di bawah ini: 
<img width="1919" height="1019" alt="Screenshot 2026-05-07 181954" src="https://github.com/user-attachments/assets/fa96af89-7efc-44bc-8ab5-e8354c4a4272" />
<img width="1918" height="981" alt="Screenshot 2026-05-07 182012" src="https://github.com/user-attachments/assets/a61fa30a-46b8-4ff6-a7c8-07223a14eecb" />
Penjelasan code: 

 def binary_search(nilai_mahasiswa, target):
digunakan untuk mencari nilai yang diinginkan.

    kiri = 0
    kanan = len(nilai_mahasiswa) - 1
kiri = indeks awal
kanan = indeks akhir data
yang digunakan sebagai batas pencarian

    tengah = (kiri + kanan) // 2
Digunakan untuk mencari posisi tengah data.

    if nilai_mahasiswa[tengah] == target:
Mengecek apakah nilai tengah sama dengan nilai yang dicari.

    elif nilai_mahasiswa[tengah] < target:
Jika nilai yang dicari lebih besar dari nilai tengah, maka pencarian berpindah ke kanan.

    kiri = tengah + 1
Batas kiri digeser ke kanan.

    else:
Jika target lebih kecil dari nilai tengah, maka pencarian pindah ke kiri.

 kanan = tengah - 1
Batas kanan digeser ke kiri.

    Jika data tidak ditemukan, program mengembalikan nilai -1.
Jika data tidak ditemukan, program mengembalikan nilai -1.
## D. Output Program
Screenshoot output:
<img width="604" height="474" alt="Screenshot 2026-05-07 180809" src="https://github.com/user-attachments/assets/d8ab2bd2-a16a-4f88-842a-bd91adbff197" />
Penjelasan output:
- Program menggunakan algoritma Binary Search untuk mencari nilai mahasiswa.
- Jumlah data yang dimasukkan = 5 mahasiswa.
- Nilai harus diinput secara urut menaik:
[60, 68, 78, 83, 88]
- Nilai yang dicari adalah 78.
- Program mencari dari data tengah.
- Posisi tengah berada di indeks 2 dengan nilai 78.
- Karena nilai tengah sama dengan nilai yang dicari, data langsung ditemukan.
- Hasil akhir: Nilai 78 ditemukan pada indeks ke-2
## LINK YOUTUBE
https://youtu.be/31H0czoi6B4
