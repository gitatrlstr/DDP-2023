def datadiri(nama, alamat, gender, umur, hoby) :
    print("nama", nama)
    print("alamat", alamat)
    print("gender", gender)
    print("umur", umur)
    print("hoby", hoby)
datadiri("Gita Tri Lestari", "Bogor", "Perempuan", "18 Tahun", "Menonton")

def cek_kelulusan(nilai):
    if nilai < 60:
        print("Gagal")
    elif 61 <= nilai <= 70:
        print("Baik")
    elif 71 <= nilai <= 80: 
        print("Sangat Baik")
    elif 81 <= nilai <= 100:
        print("Istimewa")    
    else:
        print("Tidak Lulus")
cek_kelulusan(60)

def ganjil(angka):
    for i in range(1, angka + 1, 2):
        print(i)
ganjil(100)
