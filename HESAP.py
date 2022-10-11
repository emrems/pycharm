
bilgi="""
    1::TOPLAMA İŞLEMİ
    2::ÇIKARMA İŞLEMİ
    3::ÇARPMA İŞLEEMİ
    4::BÖLME İŞLEMİ
    
    YUKARIDAKİ İŞLEMLERDEN BİRİNİ SEÇİNİZ
    

"""
print(bilgi)
while True:
    secim = int(input("Seçiminizi yapınız:"))


    if(secim == 1):
        x=int(input("deger gir "))
        y=int(input("deger gir "))
        print(x+y)
    elif (secim == 2):
        x=int(input("deger gir "))
        y=int(input("deger gir "))
        if(x<y):
            print("sonuc:",-(x-y))
        else:
            print(x - y)


    elif (secim == 3):
        x=int(input("deger gir "))
        y=int(input("deger gir "))
        print(x*y)

    elif (secim == 4):
        x=int(input("deger1 gir "))
        y=int(input("deger2 gir "))
        if(x<y):
            print("deger1 deger2 den buyuk olmalı")
            continue
        else:
            print(x / y)

    else:
        print("hata")

        break


