class Katalog:
    def __init__(self, katalog_id, judul, subjek, lokasi_penyimpanan, info):
        self.katalog_id = katalog_id
        self.perpus_items = []

    def cari(self, keyword):
        pass


class PerpusItem:
    def __init__(self, perpus_item_id, judul, subjek, lokasi_penyimpanan, info):
        self.perpus_item_id = perpus_item_id
        self.judul = judul
        self.subjek = subjek
        self.lokasi_penyimpanan = lokasi_penyimpanan
        self.info = info
        self.katalog = None 

class Pengarang:
    def __init__(self, pengarang_id, nama, info):
        self.pengarang_id = pengarang_id
        self.nama = nama
        self.info_pengarang = info 
        self.bukus = []

    def info(self):
        return self.info_pengarang

    def cari(self, keyword):
        pass


class Buku:
    def __init__(self, isbn, pengarang, judul, jumlah_halaman, ukuran):
        self.isbn = isbn
        self.pengarang = pengarang
        self.judul = judul
        self.jumlah_halaman = jumlah_halaman
        self.ukuran = ukuran
        self.perpus_item = None  

class Majalah:
    def __init__(self, volume, issue):
        self.volume = volume
        self.issue = issue
        self.perpus_item = None  


class DVD:
    def __init__(self, aktor, genre):
        self.aktor = aktor
        self.genre = genre
        self.perpus_item = None  


katalog = Katalog(1, "Katalog 1", "Kategori 1", "Lokasi 1", "Info 1")
perpus_item1 = PerpusItem(1, "Item 1", "Subjek 1", "Lokasi 1", "Info 1")
perpus_item2 = PerpusItem(2, "Item 2", "Subjek 2", "Lokasi 2", "Info 2")
pengarang = Pengarang(1, "John Doe", "Pengarang info 1")
buku = Buku("ISBN-123", pengarang, "Judul Buku", 200, "20x30 cm")
buku.perpus_item = perpus_item1
majalah = Majalah("Vol 1", "Issue 1")
majalah.perpus_item = perpus_item2
dvd = DVD("Aktor 1", "Action")
dvd.perpus_item = perpus_item2

print("Perpus Items in Katalog:")
for item in katalog.perpus_items:
    print(item.judul)

print("\nBukus by Pengarang:")
for buku in pengarang.bukus:
    print(buku.judul)

print("\nInfo Pengarang:")
print(pengarang.info())

print("\nSearch in Katalog:")
katalog.cari("Kategori 1")
