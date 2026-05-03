## PENGURUTAN JADWAL KEBERANGKATAN KENDARAAN
## A. Judul Program
Pengurutan jadwal keberangkatan kendaraan
## B. Deskripsi Singkat
Program ini digunakan untuk mengurutkan jadwal keberangkatan kendaraan berdasarkan jam menggunakan algoritma Insertion Sort. Pengguna memasukkan nama kendaraan dan jam berangkat (HH:MM), lalu program akan menampilkan data sebelum dan sesudah diurutkan dari waktu paling awal ke paling akhir.
## C. Source Code 
Screenshot Source Code di bawah ini:
<img width="1878" height="942" alt="Screenshot 2026-05-02 194938" src="https://github.com/user-attachments/assets/a83b21d0-3c93-4287-ba0f-a5743ee84e17" />
Penjelasan code

    def insertion_sort(jadwal):
->Fungsi untuk mengurutkan data jadwal.

      for i in range(1, len(jadwal)):
->Mengambil data satu per satu mulai dari indeks ke-1.

    key = jadwal[i]
->Menyimpan data yang ingin diposisikan dengan benar.

    j = i - 1
->Menentukan posisi sebelumnya untuk dibandingkan.

    while j >= 0 and jadwal[j][1] > key[1]:
->Membandingkan jam, jika lebih besar maka digeser.

    jadwal[j + 1] = jadwal[j]
->Menggeser data ke kanan.

    j -= 1
->Pindah ke data sebelumnya lagi.

    jadwal[j + 1] = key
->Menaruh data (key) di posisi yang tepat.

    return jadwal
->Mengembalikan jadwal yang sudah diurutkan.

# d. Output Program 
Screenshoot output
<img width="1542" height="603" alt="Screenshot 2026-05-02 195017" src="https://github.com/user-attachments/assets/8c02f81e-c8d7-449e-a03c-2b324bd034d7" />
Penjelasan output

- Saat memasukkan jumlah kendaraan → program menentukan berapa data yang akan diinput
- Saat input data → pengguna memasukkan nama kendaraan dan jam berangkat, lalu disimpan ke dalam list
- Saat menampilkan "Jadwal sebelum diurutkan" → data ditampilkan sesuai urutan input (Bus Tayo lalu Travel Rahma)
- Saat proses sorting → program mengurutkan data berdasarkan jam (12:23 lebih dulu dari 22:40)
- Saat menampilkan "Jadwal setelah diurutkan" → data tampil dari yang paling awal ke paling akhir (Travel Rahma lalu Bus Tayo)

# LINK YOUTUBE
https://youtu.be/riOClMF4pkI?si=FXBvqB4dbh9aXJW8
