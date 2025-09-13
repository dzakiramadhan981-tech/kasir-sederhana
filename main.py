# Function untuk menampilkan garis
def garis():
    print("=" * 40)

# Function untuk menghitung total belanja dengan diskon
def hitung_total(harga_list):
    total = sum(harga_list)
    
    # Kondisi (if-else)
    if total >= 100000:
        diskon = 0.1  # 10%
        print("Anda mendapat diskon 10%!")
    elif total >= 50000:
        diskon = 0.05  # 5%
        print("Anda mendapat diskon 5%!")
    else:
        diskon = 0
    
    total_bayar = total - (total * diskon)
    return total_bayar

# Program utama
garis()
print("   PROGRAM KASIR SEDERHANA")
garis()

harga_barang = []  # Variable untuk menyimpan harga setiap barang

while True:
    nama = input("Masukkan nama barang (ketik 'selesai' untuk berhenti): ")
    if nama.lower() == "selesai":
        break
    
    harga = int(input(f"Masukkan harga {nama}: "))
    harga_barang.append(harga)  # Simpan ke list
    
    garis()

# Hitung total
garis()
print("Daftar belanja anda:")
for i, h in enumerate(harga_barang, start=1):  # Perulangan for
    print(f"{i}. Rp{h}")

garis()
total_bayar = hitung_total(harga_barang)  # Memanggil function
print(f"Total yang harus dibayar: Rp{total_bayar}")
garis()
print("Terima kasih sudah berbelanja!")
