print ("angie\n"
        "sanur\n") 
username =""
password =""
while username != "angie" and password != "sanur":
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    if username == "angie" and password == "sanur":
        print ("TRUE")
    else:
        print ("WRONG")
    