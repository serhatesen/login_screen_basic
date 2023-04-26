print("""
*********************************
KULLANICI GIRIS EKRANI
*********************************
""")

sys_username = "root"
sys_password = "toor"

total_trial = 3

while True:
    username = input("Kullanıcı Adınızı Giriniz: ")
    password = input("Parolanızı Giriniz: ")

    if (sys_username != username and sys_password != password):
        total_trial -= 1
        print("Kullanıcı adı ve Parola Hatalı")
    elif (sys_username == username and sys_password != password):
        total_trial -= 1
        print("Parola Hatalı")
    elif (sys_username != username and sys_password == password):
        total_trial -= 1
        print("Kullanıcı Adı Hatalı")
    else:
        print("Sisteme Giriş sağlanıyor. Lütfen bekleyiniz.")
        break
    if (total_trial == 0):
        print("Deneme süresi dolmuştur.")
        break