class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def perkenalan(self):
        return f"Halo, saya {self.nama} dari jurusan {self.jurusan}"

mhs = Mahasiswa("Karina", "Informatika")
print(mhs.perkenalan())
