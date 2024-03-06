class MyClass:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

objek1 = MyClass("Ningsih Rahmawati", "B 2021", "Pendidikan Komputer", "Fakultas Keguruan dan Ilmu Pendidikan", "JL. Ottoiskandar Dinata Gg. Budiman", "Kota Samarinda")

print("Biodata Diri:")
print("Nama:", objek1.nama)
print("Kelas:", objek1.kelas)
print("Prodi:", objek1.prodi)
print("Fakultas:", objek1.fakultas)
print("Tempat Tinggal:", objek1.tempat_tinggal)
print("Asal:", objek1.asal)
