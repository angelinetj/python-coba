while True:
    pilihan_input = input("Apakah anda ingin menggunakan calculator (y/n): ")
    if pilihan_input == "y":
            num1_input = input("Masukkan nomor pertama: ")
            num2_input = input("Masukkan nomor kedua: ")
            print ("1 tambah\n"
                 "2 kurang\n"
                 "3 kali\n"
                 "4 bagi\n"
                "5 exit\n")

            try:
                     num1_input = int(num1_input)
                     num2_input = int(num2_input)
            except ValueError       :
                    print ("Value error")
            except:
                    print ("ERROR")
            else: 
                    pertanyaan = input(" apa yang ingin anda lakukan: ") 

            if pertanyaan == "1": 
                 print( "Hasil Jumlah kedua angka: ", num1_input + num2_input)
            elif pertanyaan == "2":
                print( "Hasil Pengurangan kedua angka: ", num1_input - num2_input)
            elif pertanyaan == "3":
                print( "Hasil perkalian kedua angka: ", num1_input * num2_input)
            elif pertanyaan == "4":
                print( "Hasil pembagian kedua angka: ", num1_input/num2_input )
            elif pertanyaan == "5":
                print ("EXIT")
                break 
    else: 
            print("OK" )
            break

             