class Pasien:
    def __init__(self, nama, tanggal_lahir, alamat, nomor_kontak):
        self.__nama = nama
        self.__tanggal_lahir = tanggal_lahir
        self.__alamat = alamat
        self.__nomor_kontak = nomor_kontak

    def get_nama(self):
        return self.__nama

    def tampilkan_info_pasien(self):
        print("--- Informasi Pasien ---")
        print(f"Nama Pasien   : {self.__nama}")
        print(f"Tanggal Lahir : {self.__tanggal_lahir}")
        print(f"Alamat        : {self.__alamat}")
        print(f"Nomor Kontak  : {self.__nomor_kontak}")


class Resep:
    def __init__(self, obat, dosis, petunjuk):
        self.__obat = obat
        self.__dosis = dosis
        self.__petunjuk = petunjuk

    def tampilkan_resep(self):
        print("--- Resep ---")
        print(f"Obat     : {self.__obat}")
        print(f"Dosis    : {self.__dosis}")
        print(f"Petunjuk : {self.__petunjuk}")


class PemeriksaanMata:
    def __init__(self, tanggal_pemeriksaan, tajam_penglihatan, tekanan_intraokular, resep_obat):
        self.__tanggal_pemeriksaan = tanggal_pemeriksaan
        self.__tajam_penglihatan = tajam_penglihatan
        self.__tekanan_intraokular = tekanan_intraokular
        self.__resep_obat = resep_obat

    def tampilkan_hasil_pemeriksaan_mata(self):
        print("--- Hasil Pemeriksaan Mata ---")
        print(f"Tanggal Pemeriksaan : {self.__tanggal_pemeriksaan}")
        print(f"Tajam Penglihatan   : {self.__tajam_penglihatan}")
        print(f"Tekanan Intraokular : {self.__tekanan_intraokular}")
        self.__resep_obat.tampilkan_resep()


class PemeriksaanLapangan:
    def __init__(self, tanggal_pemeriksaan, hasil_pemeriksaan):
        self.__tanggal_pemeriksaan = tanggal_pemeriksaan
        self.__hasil_pemeriksaan = hasil_pemeriksaan

    def tampilkan_hasil_pemeriksaan_lapangan(self):
        print("--- Hasil Pemeriksaan Lapangan ---")
        print(f"Tanggal Pemeriksaan : {self.__tanggal_pemeriksaan}")
        print(f"Hasil Pemeriksaan   : {self.__hasil_pemeriksaan}")


pasien1 = Pasien("Indra Kusuma", "19-03-2002", "Jl. Jend Sudirman", "082133651063")
pasien1.tampilkan_info_pasien()  

resep_obat = Resep("Obat Tetes Mata", "2 tetes", "3 kali sehari")

pemeriksaan_mata = PemeriksaanMata("01-02-2024", "20/20", "15 mmHg", resep_obat)
pemeriksaan_mata.tampilkan_hasil_pemeriksaan_mata()

pemeriksaan_lapangan = PemeriksaanLapangan("01-02-2024", "Normal")
pemeriksaan_lapangan.tampilkan_hasil_pemeriksaan_lapangan()