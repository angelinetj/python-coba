flowers = []

class Flower:
    def __init__(self,nama,kelopak,harga):
        self.nama = nama
        self.kelopak = kelopak
        self.harga = harga

        flowers.append(self)

    def bunga(self):
        print( "Namanya bunganya adalah", self.nama, "\n Jumlah kelopaknya sebanyak" ,self.kelopak, "\n Harga bunganya adalah", self.harga)

    @classmethod
    def new_flower(cls):
        nama = input("Masukkan Nama bunga:")
        kelopak = input("Masukkan Jumlah Kelopak Bunga:")
        harga = int(input("Masukkan Harga Bunga:"))

        return cls(nama,kelopak,harga)

tanya = "y"

while tanya == "y":
    Flower.new_flower()
    pilihan_input = input("Gunakkan lagi? (y/n): ")
    if pilihan_input == "n":
        tanya = "n"

for x in flowers:
    x.bunga()



