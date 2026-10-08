import json

def muat_data():
    with open("nilai_mahasiswa.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def simpan_data(data):
    with open("nilai_mahasiswa.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def tampilkan_nilai(data):
    print("\n" + "-" * 40)
    print(f"{'NIM'} | {'Nama'} | {'Nilai'}")
    print("\n" * 40)

    if not data:
        print("Belum ada data nilai yang tersimpan")
    else:
        for mahasiswa in data:
            print(f"{mahasiswa['NIM']} | {mahasiswa['Nama']} | {mahasiswa['Nilai']}")
    print("-" * 40)

def tambah_nilai(data):
    print("\n--- Tambah Data Nilai Baru ---")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama Mahasiswa: ")
    nilai = float(input("Masukkan nilai (0-100): "))

    data_baru = {
        "NIM": nim,
        "Nama": nama,
        "Nilai": nilai
    }

    data.append(data_baru)
    simpan_data(data)
    print("\n Data nilai berhasil ditambahkan!")

def main():
    data_mahasiswa = muat_data()

    while True:
        print("\n--- SISTEM PENCATATAN NILAI MAHASISWA ---")
        print("1. Tampilkan Histori Nilai")
        print("2. Tambahkan Data Nilai Baru")
        print("3. keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            tampilkan_nilai(data_mahasiswa)
        elif pilihan == "2":
            tambah_nilai(data_mahasiswa)
        elif pilihan == "3":
            print("\nTerima kasih")
            break
        else:
            print("Pilihan Tidak Valid.")

if __name__ == "__main__":
    main()

