# Catatan List
print("| Catatan List |".center(30, "=") + "\n")

# Jenis-Jenis List
print("| Jenis-Jenis List | ".center(30, "="))

# 1. List int/float
print("| 1. List int/float | ".center(30, "X"))
data_angka = [1.2,2,3,4,5]
print(f"contoh list angka = {data_angka}")

# 2. List str
print("| 2. List str | ".center(30, "X"))
data_str = ["Ayam", "Sapi", "Kucing"]
print(f"contoh list str = {data_str}")

# 3. List boolean
print("| 3. List boolean | ".center(30, "X"))
data_boolean = [True, False, True]
print(f"contoh list boolean = {data_boolean}")

# 4. List campuran
print("| 4. List campuran | ".center(30, "X"))
data_campuran = ["Ayam", False, 1.4, "Awkwkwk"]
print(f"contoh list campuran = {data_campuran}\n")

# Mengetahui Jumlah Data Pada List "GUNAKAN len(nama_variable)"
print("| Mengetahui Jumlah Data Pada list |".center(46, "="))
data = ["a", "b", "c", "d", "e"]
print(f"Data: {data}")
jumlah_data = len(data)
print(f"Jumlah data: {jumlah_data}\n")

# Mengetahui Urutan Keberapa Sebuah Data
print("Mengetahui Urutan ke- Data Pada list".center(46, "-"))
print(f"Data: {data}")
# Data Pertama Dimulai dari 0 (Sesuai Index)
datake0 = data[0]
print(f"Data ke 0: {datake0}")
# Mencari data terakhir
print("Mencari Data terakhir sebuah data(khusus diakhir)".center(55,"-"))
print(f"Data: {data}")
dataakhir = data[-1]
print(f"Data terakhir: {dataakhir}")
# Menambahkan Sebuah Data Pada Data, gunakan sebuah_data.insert(nambahin setelah urutan ke-, mau nambahin apa)
print("Nambahin Data (Custom/dimana aja)".center(50,"-"))
print(f"Data normal: {data}")
data.insert(1,"anjay")
print(f"Nambah data: {data}")
# Menambahkan Sebuah Data pada Akhir Data, gunakan: sebuah_data.append("nama data")
print("Nambahin Data pada akhir sebuah data(khusus diakhir)".center(60,"-"))
print(f"Data normal: {data}")
data.append("Kiwkiw")
print(f"Nambah data diakhir(khusus): {data}")
# Menggabungkan Suatu Data Dengan Data Lainnya, gunakan: sebuah_data.extend("nama data lain")
print("Menggabungkan Suatu Data Dengan Data Lainnya".center(60,"-"))
data_baru = [1,2,3,4]
data.extend(data_baru)
print(f"Gabungin 2 data: {data}")
# Mengganti sebuah data pada sebuah data, gunakan: data[nomor data]
print("Mengganti sebuah data".center(60,"-"))
print(f"Data awal: {data_baru}")
data_baru[1] = "TerbaruXD"
print(f"Data yg diubah: {data_baru}")
# Menghapus suatu data, gunakan: nama_data.remove(nama data)
print("Menghapus sebuah data".center(60,"-"))
print(f"Data awal: {data_baru}")
data_baru.remove("TerbaruXD")
print(f"Data yg diubah: {data_baru}")
# Menghapus data terakhir (khusus data terakhir), gunakan: 
print("Menghapus sebuah data (Khusu Terakhir)".center(60,"-"))
print(f"Data awal: {data_baru}")
data_baru.pop()
print(f"Data yg diubah: {data_baru}")




