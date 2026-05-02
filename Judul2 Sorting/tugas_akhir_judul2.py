def insertion_sort(jadwal):
    for i in range(1, len(jadwal)):
        key = jadwal[i]
        j = i - 1

        while j >= 0 and jadwal[j][1] > key[1]:
            jadwal[j + 1] = jadwal[j]
            j -= 1
        
        jadwal[j + 1] = key

    return jadwal

n = int(input("Masukkan jumlah kendaraan: "))

jadwal = []

for i in range(n):
    print(f"\nData ke-{i+1}")
    nama = input("Nama kendaraan: ")
    jam = input("Jam berangkat (HH:MM): ")
    
    jadwal.append((nama, jam))

print("\nJadwal sebelum diurutkan:")
for data in jadwal:
    print(data[0], "-", data[1])

jadwal_urut = insertion_sort(jadwal)

print("\nJadwal setelah diurutkan:")
for data in jadwal_urut:
    print(data[0], "-", data[1])