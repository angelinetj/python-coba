print('Pesan apa aja mbak?')
print('Mbak sudah pesan')

pesanan_1 = ['es teh manis','nasi pecel','sambal bawang']
for m in range(len(pesanan_1)):
    print(m+1, pesanan_1[m]) 

tambahan =input('Ada tambahan mbak? (y/n): ')
while tambahan == 'y':
    pesanan_2 = input('Mau tambah apa mbak? ')
    print('Saya ulang pesanannya ya')
    pesanan_1.append(pesanan_2)
    for m in range(len(pesanan_1)):
        print(m+1, pesanan_1[m])
    tambahan =input('Ada tambahan mbak? (y/n): ')
else:
    print ("TERIMA KASIH")