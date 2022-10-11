#emre almamış
#b210109029
#bilgisayar muh. 1. sınıf
#hesap makinesi oluştrma ve parola giriş sistemi oluşturma

giriş_paneli="""
          KULLANICI GİRİŞ PANELİNE HOŞGELDİNİZ
          
          LUTFEN KULLANICI ADI VE ŞİFRENİZİ GİRİNİZ


"""
print(giriş_paneli)
import string

buyuk_harf = [chr(k) for k in range(65, 91)]
kucuk_harf = string.ascii_lowercase
rakam = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sembol = string.punctuation
kontrol1 = 0
kontrol2 = 0
kontrol3 = 0
kontrol4 = 0
hak = 0
while hak < 5:


    kullanıc_adı = input("lutfen kullanıcı adı  giriniz ")
    if len(kullanıc_adı)<16:
        print("kullanıcı adı  karakteri yeterli degil en az 16 karakter olmalı")
        continue

    for i in kullanıc_adı:
        if (i in buyuk_harf):
            kontrol1 = kontrol1 + 1
        elif (i in kucuk_harf):
            kontrol2 = kontrol2 + 1
        elif (i in rakam):
            kontrol3 = kontrol3 + 1
        elif (i in sembol):
            kontrol4 = kontrol4 + 1

    kontrol = (kontrol1 < 1) or (kontrol2 < 1) or (kontrol3 < 1) or (kontrol4 < 1)

    if (kontrol == 1):

        if (kontrol1 < 1):
            print("kullanıcı adı buyuk harf içermeli lütfen buyuk harf giriniz")
        if (kontrol2 < 1):
            print("kullanıcı adı kucuk harf içermeli lutfen küçük harf giriniz")

        if (kontrol3 < 1):
            print("   kullanıcı adı rakam içermeli lutfen rakam giriniz")
        if (kontrol4 < 1):
            print("kulanıcı adı sembol içermeli lütfen sembol giriniz")
    else:
        print("tebrikler giriş yapabilirsiniz")
        break
    hak = hak + 1
    if(hak==5):
        print("çıkış yapılıyor")
        break
    else:
        continue






hak1=0
buyuk_kontrol=0
kucuk_kontrol=0
rakam_kontrol=0
kontrol_sembol=0

while hak1<3:
    hak1=hak1+1
    sifre = input("şifreyi giriniz: ")
    if(len(sifre)<8 or len(sifre)>24):
        print("şifreniz 8 ila 24 karakter arasında olmalıdır")
        continue

    for k in sifre:
        if(k in buyuk_harf):
            buyuk_kontrol=buyuk_kontrol+1
        elif(k in kucuk_harf):
            kucuk_kontrol=kucuk_kontrol+1
        elif(k in rakam ):
            rakam_kontrol=rakam_kontrol+1
        elif(k in sembol):
            kontrol_sembol=kontrol_sembol+1

    kontroller=(buyuk_kontrol<1) or (kucuk_kontrol<1) or (rakam_kontrol<1) or (kontrol_sembol<1)

    if(kontroller==1):
        if(kucuk_kontrol<1):
            print("kucuk harf kullanmalısın")
        if(buyuk_kontrol<1):
            print("buyuk harf kullanmalısın")
        if(rakam_kontrol<1):
            print("rakam kullanmalısın ")
        if(kontrol_sembol<1):
            print("sembol kullanmalsın")
    else:
        print("tebrikler başaşrı ile giriş yaptınız")
        break




bilgi = """
    1::TOPLAMA İŞLEMİ
    2::ÇIKARMA İŞLEMİ
    3::ÇARPMA İŞLEEMİ
    4::BÖLME İŞLEMİ

    YUKARIDAKİ İŞLEMLERDEN BİRİNİ SEÇİNİZ


"""
print(bilgi)
while True:
    secim = int(input("Seçiminizi yapınız:"))

    if (secim == 1):
        print("toplama işlemini seçtiniz")
        toplama = input("arada + işareti olmalı:\n")
        print(eval(toplama))
    elif (secim == 2):
        print("cıkarma işlemini seçtiniz ")
        cikarma = input("arada - işareti olmalı:\n")
        print(eval(cikarma))
    elif (secim == 3):
        print("çarpma işlemini seçtiniz ")
        carpma = input("arada * işareti olmalı:\n")
        print(eval(carpma))
    elif (secim == 4):
        print("bölme işlemini seçtiniz ")
        bolme = input("araada / işareti olmalı:\n")
        print(eval(bolme))
    else:
        print("hata")

        break































