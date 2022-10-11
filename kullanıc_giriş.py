kullanıcı_adı="emre_almamıs"
sifre=12345

hak=0
while hak<4:
    kul_adı=input("kullanıcı adını giriniz: ")
    sifre_al=int(input("şifreyi giriniz "))

    if(kul_adı==kullanıcı_adı and sifre==sifre_al):
        print("hosgeldin")
    else:
        if(kul_adı!=kullanıcı_adı):
            print("kullanıcı adı yanlış")
            hak=hak+1
        if(sifre!=sifre_al):
            print("şifre yanlış")
            hak=hak+1
        elif(kul_adı!=kullanıcı_adı and sifre!=sifre_al):
            print("kullanıcı adı ve şifre yanlış")
            hak=hak+1
    if(hak==4):
        print("sistemden çıkılıyor")
        break
    else:
        continue





