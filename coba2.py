import random
real_ans = random.randint(1,10) 

print ("tebak angka antara 1 sampai 10")

num_input = input("berapa tebakan lu?")
    print ("num_input") 
while  num < real_ans:
    jawab = int(input("terlalu kecil"))
while num > real_ans:
    jawab = int(input("terlalu besar"))
else:
    print ("ok")