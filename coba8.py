siswas = []

class siswa:
    def __init__(self,name,age,alamat):
        self.name = name
        self.age = age
        self.alamat = alamat

        siswas.append(self)
    
    def perkenalan(self):
        print(self.name, self.age, self.alamat)

    @classmethod
    def new_siswa(cls):
        name = input("Masukkan nama siswa: ")
        age = input("Masukkan umur siswa:" )
        alamat = input("Masukkan alamat siswa:")

        return cls(name, age, alamat)

siswa1 = siswa("kenny","17","gading")
siswa1.perkenalan()

for x in range(3):
    siswa= siswa.new_siswa()

for siswa in siswas:
    print(siswa)