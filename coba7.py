print (" ===Tube Calculator===")

tabungs = []
class Tabung:
    def __init__(self, jari, tinggi, hasil ):
        self.jari = jari
        self.tinggi = tinggi
        self.hasil = hasil 
        tabungs.append(self)

    def hitung(self):
        print(" Jari-Jari tabung", self.jari, "Tinggi tabung " , self.tinggi, 
        "Luas lingkaran adalah", self.luas, " Volume lingkaran adalah" ,self.volume )

    @classmethod
    def hitung_baru(cls):
        jari = input("Masukkan jari-jari tabung: ")
        tinggi = input("Masukkan tinggi tabung: ")
        print ("1 Hitung luas lingkaran Alas\n"
                 "2 Hitung volume tabung\n")
        try:
            jari = int(jari)
            tinggi = int(tinggi)
        except ValueError       :
            print ("Value error")
        except:
            print ("ERROR")
        else: 
            pertanyaan = input("apa yang ingin dihitung: ") 
            radius = 3.14 
            if pertanyaan == "1": 
                luas = 2 * radius * jari
                print(f'Luas Lingkaran : {luas} ')
            elif pertanyaan == "2":
                volume = radius * (jari**2) * tinggi
                print(f'Volume Lingkaran : {volume} ')
            return cls (jari,tinggi,luas,volume )

tanya = "y"

while tanya == "y":
    Tabung.hitung_baru()
    pilihan_input = input("Mau menggunakan Calculator (y/n): ")
    if pilihan_input == "n":
        tanya = "n"

for x in tabungs:
    x.hitung()


