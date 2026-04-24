#soal 1
#tipe data integer hanya bisa di isi oleh angka,dan bilangan bulat
#tipe data float hanya bisa di isi oleh bilangan desimal
#tipe data string hanya bisa di isi oleh teks 
#tipe data boolean hanya bisa di isi oleh kondisi true/false

Nama = input("Nama mahasiswa :")
Umur = int(input("Umur :"))
IPK = int(input("IPK :"))

print("nama :", Nama)
print("umur :", Umur, "tahun")
print("IPK :", IPK)
print("\n")

#soal 2
Nama_kandang = "kandang ayam"
print("nama kandang :", Nama_kandang)
Jumlah_ayam = 25
print("jumlah ayam:", Jumlah_ayam)
total_telur = 0
hari = 0

rata_rata = total_telur / Jumlah_ayam

while hari < 7:
    harian = int(input(f"Masukkan jumlah telur hari ke-{hari+1}: "))
    total_telur += harian
    hari += 1
    print("total telur saat ini", total_telur)
    
    rata_rata = total_telur / Jumlah_ayam
    if rata_rata >= 0.8:
        print("produktif tinggi")
    elif rata_rata >= 0.5:   
        print("produksi sedang")
    else:                    
        print("produktif rendah")
print("total telur selama 7 hari :", total_telur)
print("rata rata :",rata_rata)


