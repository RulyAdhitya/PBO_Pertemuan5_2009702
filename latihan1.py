# Polymorphism dengan class
class Sapi:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def deskripsi(self):
        print(
            f"Jika saya Sapi. Nama saya adalah {self.nama}. Umur saya {self.umur} tahun.")

    def bersuara(self):
        print("Moo")


class Kambing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def deskripsi(self):
        print(
            f"Jika saya kambing. Nama saya adalah {self.nama}. Umur saya {self.umur} tahun.")

    def bersuara(self):
        print("Mbeee")


sapi1 = Sapi("Grandong", 2.5)
kambing1 = Kambing("Shaun", 4)

for animal in (sapi1, kambing1):
    animal.bersuara()
    animal.deskripsi()
    animal.bersuara()
