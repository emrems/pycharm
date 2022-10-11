bil_muh=[]
mekatronik_muh=[]
makina_muh=[]

def silme_isim():
    x=int(input("seçimini yapınız"))
    if x==1:
            print("BİLGİSAYAR MUHENDİSLİĞİ SEÇTİN")

            isim = input("silinecek ismi gir")
            index = 0
            for i in bil_muh :
                if isim in i:
                    bil_muh.pop(index)
            index = index + 1
            print(bil_muh)
    elif x == 2:
        print("MEKATRONİK MÜHENDİSLİĞİ SEÇTİN")
        isim1 = input("silinecek ismi gir")
        indexx = 0
        for eleman in mekatronik_muh:
            if isim1 in eleman:
                mekatronik_muh.pop([indexx][0])
            indexx = indexx + 1
        print(mekatronik_muh)
    else:
        print("MAKİNA MÜHENDİSLİĞİ")
        isim2 = input("silinecek isimi gir")
        indexxx = 0
        for eleman2 in makina_muh:
            if isim2 in eleman2:
                makina_muh.pop([indexxx][0])
            indexxx = indexxx + 1
        print(makina_muh)


def ortalama(vize,odev,final):
    while True:
        ort = vize * 0.3 + odev * 0.2 + final * 0.5

        if ort < 0 or ort > 100:
            print("YANLIŞ ORTALAMA!!!")
            break

        else:
            durum5 = "kaldı"
            if ort >= 90 and ort <= 100:
                durum5 = "AA"
            elif ort < 90 and ort >= 85:
                durum5 = "BA"
            elif ort < 85 and ort >= 80:
                durum5 = "BB"
            elif ort >= 75 and ort < 80:
                durum5 = "CB"
            elif ort >= 70 and ort < 75:
                durum5 = "CC"
            elif ort >= 65 and ort < 70:
                durum5 = "DC"
            elif ort >= 60 and ort < 65:
                durum5 = "DD"
            elif ort >= 50 and ort < 60:
                durum5 = "FD"
            else:
                durum5 = "FF"
        return durum5


def secim():
    while True:
        print(""""
        1:BİLGİSAYAR MÜHENDİSLİĞİ
        2:MEKATRONİK MÜHENDİSLİĞİ
        3:MAKİNA MÜHENDİSLİĞİ
        4:ÇIKIŞ
        """)
        sec=input("SEÇİM YAPINIZZ")
        try:
            sec=int(sec)
        except ValueError:
            print("rakam giriniz")
        if sec==1:
            print("BİLGİSAYAR MÜHENDİSLİĞİ SEÇTİNİZ")
        elif sec==2:
            print("MEKATRONİK MÜHENDİSLİĞİ SEÇTİNİZ")
        elif sec==3:
            print("MAKİNA MÜHENDİSLİĞİ SEÇTİNİZ")
        else:
            print("ÇIKIŞ YAPILIYOR")
            break
    return sec


while True:
    print(""""
    1:BİLGİSAYAR MÜHENDİSLİĞİ
    2:MEKATRONİK MÜHENDİSLİĞİ
    3:MAKİNA MÜHENDİSLİĞİ
    4:DİĞER İŞLEMLER
    5:ÇIKIŞ
    """)
    secim1=input("BİR İŞLEM SEÇİNİZ")
    try:
        secim1=int(secim1)
    except ValueError:
        print("LÜTFEN RAKAM GİRİNİZ")

    if secim1==1:
        print("BİLGİSAYAR MÜHENDİSLİĞİ SEÇTİNİZ")
        ogr_bil=input("OGRENCİ SAYINI GİRİNİZ")
        try:
            ogr_bil=int(ogr_bil)
        except ValueError:
            print("RAKAM GİR")
            break

        ders_bil = input("DERS SAYISINI GİRİNİZ")
        try:
            ders_bil=int(ders_bil)
        except ValueError:
            print("RAKAM GİR")
            break


        if ogr_bil<0 and ogr_bil>20:
            print("LUTFEN 5 İLA 20 ARASI ÖĞRENCİ GİRİNİZ")
            break
        else:
            for i in range(ogr_bil):
                ogr_ad_bil = input("ÖĞRENCİ ADI GİRİNİZ")
                ogr_bil_no=input("ÖĞRENCİNİN NUMARASINI GİRİNİZ")

                for j in range(ders_bil):
                    ders_bilgisayar=input("DERS ADI GİR")
                    bil_vize=int(input("VİZE NOTUNU GİRİNİZ"))
                    bil_odev=int(input("ODEV NOTUNU GİRİNİZ"))
                    bil_final=int(input("FİNAL NOTUNU GİRİNİZ"))


                    top_bil=[ogr_ad_bil,ogr_bil_no,bil_vize,bil_odev,bil_final,ortalama(bil_vize,bil_odev,bil_final)]
                    bil_muh.append(top_bil)
            print(bil_muh)
    elif secim1==2:
        print("MEKATRONİK MÜHENDİSLİĞİ")
        ogr_mek=input("ÖĞRENCİ SAYISINI GİRİNİZ")
        try:
            ogr_mek=int(ogr_mek)
        except ValueError:
            print("RAKAM GİR")
            break
        ders_mek=input("DERS SAYISINI GİRİNİZ")
        try:
            ders_mek=int(ders_mek)
        except ValueError:
            print("RAKAM GİR")
            break
        if ogr_mek<0 and ogr_mek>20:
            print("5 İLA 20 ARASI OGRENCİ GİRİNİZ")
            break
        else:
            for k in range(ogr_mek):
                ad_mek=print("OGRENCİ ADINI GİR")
                no_mek=input("OGRENCİ NUMARASI GİR")
                try:
                    no_mek=int(no_mek)
                except ValueError:
                    print("RAKAM GİR")
                    break
                for h in range(ders_mek):
                    ders_ad_mek=input("DERS ADI GİR")
                    vize_mek=int(input("VİZE NOTUNU GİR"))
                    odev_mek=int(input("ODEVV NOTLARINI GİR"))
                    final_mek=int(input("FİNAL NOTLARININ  GİR"))
                    top_mek=[ad_mek,no_mek,ders_ad_mek, vize_mek,odev_mek,final_mek,ortalama(vize_mek,odev_mek,final_mek)]
                    mekatronik_muh.append(top_mek)
            print(mekatronik_muh)
    elif secim1==3:
        print("MAKİNA MÜHENDİSLİĞİ")
        ogr_mak = input("ÖĞRENCİ SAYISINI GİRİNİZ")
        try:
            ogr_mak = int(ogr_mak)
        except ValueError:
            print("RAKAM GİR")
            break
        ders_mak = input("DERS SAYISINI GİRİNİZ")
        try:
            ders_mak = int(ders_mak)
        except ValueError:
            print("RAKAM GİR")
            break
        if ogr_mak < 0 and ogr_mak > 20:
            print("5 İLA 20 ARASI OGRENCİ GİRİNİZ")
            break
        else:
            for k in range(ogr_mak):
                ad_mak = print("OGRENCİ ADINI GİR")
                no_mak = input("OGRENCİ NUMARASI GİR")
                try:
                    no_mak = int(no_mak)
                except ValueError:
                    print("RAKAM GİR")
                    break
                for h in range(ders_mak):
                    ders_ad_mak = input("DERS ADI GİR")
                    vize_mak = int(input("VİZE NOTUNU GİR"))
                    odev_mak = int(input("ODEVV NOTLARINI GİR"))
                    final_mak = int(input("FİNAL NOTLARININ  GİR"))
                    top_mak = [ad_mak, no_mak, ders_ad_mak, vize_mak, odev_mak, final_mak,
                               ortalama(vize_mak, odev_mak, final_mak)]
                    makina_muh.append(top_mak)
            print(makina_muh)
    elif secim1==4:
        print("DİĞER İŞLEMLER")
        print("""
                      1:OGRENCİ EKLEME
                      2:SİLME
                      3:OGRENCİ NOT GUNCELLEME
                      4:OGRENCİ NO GUNCELLEME
                      5:ÇIKIŞ
                      6:OGRENCİ AD GUNCELLEME""")
        secim2=input("SEÇİM YAPINIZ")
        try:
            secim2=int(secim2)
        except ValueError:
            print("RAKAM GİRİNİZ")
            break
        if secim2==1:
            print("OGRENCİ EKLEME İŞLEMLERİ")
            secim3=secim()
            if secim3==1:
                print("BİLGİSAYAR MÜHENDİSLİĞİ ÖĞRENCİ EKLEME BÖLÜMÜ")
                ekle_bil_ogr=int(input("EKLEMEK İSTEDİĞİNİZ OGRENCİ ADEDİ GİRİNİZ"))
                ekle_bil_ders=int(input("DERS SAYISI GİRİNİZ"))
                for h in range(ekle_bil_ders):
                    ekle_bil_ad=input("AD GİRİNİZ")
                    ekle_bil_no=input("NUMARA GİR")
                    try:
                        ekle_bil_no=int(ekle_bil_no)
                    except ValueError:
                        print("RAKAM GİR")
                        break
                    for j in range(ekle_bil_ders):
                        ekle_bil_ders_ad=input("DERS ADINI GİRİNİZ")
                        ekle_bil_vize=int(input("VİZE GİR"))
                        ekle_bil_odev=int(input("ODEV NOTUNU GİR"))
                        ekle_bil_final=int(input("FİNAL GİRİNİZ"))
                        ekle_top_bil=[ekle_bil_ad,ekle_bil_no,ekle_bil_ders_ad,ekle_bil_vize, ekle_bil_odev,ekle_bil_final,ortalama(ekle_bil_vize,ekle_bil_odev,ekle_bil_final) ]
                        bil_muh.append(ekle_top_bil)
                print(bil_muh)
            elif secim3==2:
                print("MEKATRONİK MÜHENDİSLİGİ SEÇTİNİZ")
                print("MEKATRONİK MÜHENDİSLİĞİ OGRENCİ EKLEME")
                ekle_mek_ogr = int(input("EKLEMEK İSTEDİĞİNİZ OGRENCİ ADEDİ GİRİNİZ"))
                ekle_mek_ders = int(input("DERS SAYISI GİRİNİZ"))
                for n in range(ekle_mek_ogr):
                    ekle_mek_ad = input("AD GİRİNİZ")
                    ekle_mek_no = input("NUMARA GİR")
                    try:
                        ekle_mek_no = int(ekle_mek_no)
                    except ValueError:
                        print("RAKAM GİR")
                        break
                    for j in range(ekle_mek_ders):
                        ekle_mek_ders_ad = input("DERS ADINI GİRİNİZ")
                        ekle_mek_vize = int(input("VİZE GİR"))
                        ekle_mek_odev = int(input("ODEV NOTUNU GİR"))
                        ekle_mek_final = int(input("FİNAL GİRİNİZ"))
                        ekle_top_mek = [ekle_mek_ad, ekle_mek_no, ekle_mek_ders_ad, ekle_mek_vize, ekle_mek_odev,
                                        ekle_mek_final, ortalama(ekle_mek_vize, ekle_mek_odev, ekle_mek_final)]
                        mekatronik_muh.append(ekle_top_mek)
                print(mekatronik_muh)
            elif secim3==3:
                print("MAKİNA MUHENDİSLİĞİ EKLEME BOLUMU")
                ekle_mak_ogr = int(input("EKLEMEK İSTEDİĞİNİZ OGRENCİ ADEDİ GİRİNİZ"))
                ekle_mak_ders = int(input("DERS SAYISI GİRİNİZ"))
                for e in range(ekle_mak_ogr):
                    ekle_mak_ad = input("AD GİRİNİZ")
                    ekle_mak_no = input("NUMARA GİR")
                    try:
                        ekle_mak_no = int(ekle_mak_no)
                    except ValueError:
                        print("RAKAM GİR")
                        break
                    for r in range(ekle_mak_ders):
                        ekle_mak_ders_ad = input("DERS ADINI GİRİNİZ")
                        ekle_mak_vize = int(input("VİZE GİR"))
                        ekle_mak_odev = int(input("ODEV NOTUNU GİR"))
                        ekle_mak_final = int(input("FİNAL GİRİNİZ"))
                        ekle_top_mak = [ekle_mak_ad, ekle_mak_no, ekle_mak_ders_ad, ekle_mak_vize, ekle_mak_odev,
                                        ekle_mak_final, ortalama(ekle_mak_vize, ekle_mak_odev, ekle_mak_final)]
                        makina_muh.append(ekle_top_mak)
                print(makina_muh)
            else:
                print("ÇIKIŞ YAPILIYOR")
                break
        elif secim2==2:
            print("SİLME İŞLEMLERİ")
            silme_isim()
        elif secim2==3:
            print("NOT GÜNCELLEME")


            print("BİLGİSAYAR MÜHENDİSLİĞİ NOT GUNCELLEME")
            not_bilgisayar=int(input("SİLMEK İSTEDİĞİNİZ NOTU GİRİNİZ"))
            yeni_not_bilgisyar=int(input("YENİ NOTUNU GİRİNİZ"))
            sayac=0
            for gez in bil_muh:
                if not_bilgisayar in gez:
                    bil_muh[sayac][3]=yeni_not_bilgisyar
                    bil_muh[sayac][6]=ortalama(yeni_not_bilgisyar,bil_odev,bil_final)
                    sayac=sayac+1
            print(bil_muh)















