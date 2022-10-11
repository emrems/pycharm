bilgisayar = []
makine = []
elektronik = []


print("""
*******
*   NOT GİRİŞ   *
*   PROGRAMI    *
*******
""")

while True:
    print("""
    1-Bilgisayar Mühendisliği
    2-Makine Mühendisliği
    3-Elektronik Mühendisliği
    4-Diğer İşlemler
    5-Çıkış
    """)
    bolum_secimi = input("Lütfen bir seçim yapınız:")

    try:
        bolum_secimi = int(bolum_secimi)
    except ValueError:
        print("Lütfen bir sayı giriniz.")

    if (bolum_secimi == 5):
        print("Programdan çıkış yapılıyor...")
        break

    elif (bolum_secimi == 1):
        bil_ogr_index = 0
        bil_ders_index = 0
        bil_ders = input("Lütfen ders sayisini giriniz:")
        try:
            bil_ders = int(bil_ders)
        except ValueError:
            print("Lütfen bir sayi giriniz")
            continue

        bil_ogr = input("Lütfen toplam öğrenci sayısını giriniz:")
        try:
            bil_ogr = int(bil_ogr)
        except ValueError:
            print("Lütfen bir sayi giriniz")
            continue

        if (bil_ogr < 5 or bil_ogr > 20):
            print("Geçersiz bir büyüklük girdiniz.")
            continue
        else:
            for i in range(0, bil_ogr):
                bil_ogr_ad = input("Lütfen ogrenci adini giriniz:")
                bil_ogr_no = input("Lütfen ogrenci numarasini giriniz:")
                bil_ogr_index += 1
                for j in range(0, bil_ders):
                    bil_ad = input("Lütfen ders adini giriniz:")
                    bil_ogr_final = input("Lütfen final notunu giriniz:")
                    bil_ogr_vize = input("Lütfen vize notunu giriniz:")
                    try:
                        bil_ogr_final = float(bil_ogr_final)
                        bil_ogr_vize = float(bil_ogr_vize)
                    except ValueError:
                        print("Lütfen bir ondalık sayı veya sayı giriniz")
                        continue
                    bil_ogr_ort = (0.7*bil_ogr_final) + (0.3*bil_ogr_vize)

                    if (bil_ogr_ort < 0 or bil_ogr_ort > 100):
                        print("Hatalı bir ortalama hesaplandı")
                        break

                    if (bil_ogr_ort >= 90 or bil_ogr_ort <= 100):
                        bil_harf = "AA"
                        bil_ort = 4.00
                    elif (bil_ogr_ort >= 85 or bil_ogr_ort < 90):
                        bil_harf = "BA"
                        bil_ort = 3.50
                    elif (bil_ogr_ort >= 80 or bil_ogr_ort < 85):
                        bil_harf = "BB"
                        bil_ort = 3.00
                    elif (bil_ogr_ort >= 75 or bil_ogr_ort < 80):
                        bil_harf = "CB"
                        bil_ort = 2.50
                    elif (bil_ogr_ort >= 70 or bil_ogr_ort < 75):
                        bil_harf = "CC"
                        bil_ort = 2.00
                    elif (bil_ogr_ort >= 65 or bil_ogr_ort < 70):
                        bil_harf = "DC"
                        bil_ort = 1.50
                    elif (bil_ogr_ort >= 60 or bil_ogr_ort < 65):
                        bil_harf = "DD"
                        bil_ort = 1.00
                    elif (bil_ogr_ort >= 50 or bil_ogr_ort < 60):
                        bil_harf = "FD"
                        bil_ort = 0.50
                    elif (bil_ogr_ort >= 0 or bil_ogr_ort < 50):
                        bil_harf = "FF"
                        bil_ort = 0.00
                    bil_ders_index += 1
                    bilgisayar.append([bil_ad, bil_ogr_ad, bil_ogr_no, bil_ogr_final, bil_ogr_vize, bil_ogr_ort, bil_harf, bil_ort])

    elif (bolum_secimi == 2):
        mak_ogr_index = 0
        mak_ders_index = 0
        mak_ders = input("Lütfen ders sayisini giriniz:")
        try:
            mak_ders = int(mak_ders)
        except ValueError:
            print("Lütfen bir sayi giriniz")
            continue
        mak_ogr = input("Lütfen toplam öğrenci sayısını giriniz:")
        try:
            mak_ogr = int(mak_ogr)
        except ValueError:
            print("Lütfen bir sayi giriniz")
            continue

        if (mak_ogr < 5 or mak_ogr > 20):
            print("Geçersiz bir büyüklük girdiniz.")
            continue
        else:
            for i in range(0, mak_ogr):
                mak_ogr_ad = input("Lütfen ogrenci adini giriniz:")
                mak_ogr_no = input("Lütfen ogrenci numarasini giriniz:")
                mak_ogr_index += 1
                for j in range(0, mak_ders):
                    mak_ad = input("Lütfen ders adini giriniz:")
                    mak_ogr_final = input("Lütfen final notunu giriniz:")
                    mak_ogr_vize = input("Lütfen vize notunu giriniz:")
                    try:
                        mak_ogr_final = float(mak_ogr_final)
                        mak_ogr_vize = float(mak_ogr_vize)
                    except ValueError:
                        print("Lütfen bir ondalık sayı veya sayı giriniz")
                        continue
                    mak_ogr_ort = (0.7*mak_ogr_final) + (0.3*mak_ogr_vize)

                    if (mak_ogr_ort < 0 or mak_ogr_ort > 100):
                        print("Hatalı bir ortalama hesaplandı")
                        break

                    if (mak_ogr_ort >= 90 or mak_ogr_ort <= 100):
                        mak_harf = "AA"
                        mak_ort = 4.00
                    elif (mak_ogr_ort >= 85 or mak_ogr_ort < 90):
                        mak_harf = "BA"
                        mak_ort = 3.50
                    elif (mak_ogr_ort >= 80 or mak_ogr_ort < 85):
                        mak_harf = "BB"
                        mak_ort = 3.00
                    elif (mak_ogr_ort >= 75 or mak_ogr_ort < 80):
                        mak_harf = "CB"
                        mak_ort = 2.50
                    elif (mak_ogr_ort >= 70 or mak_ogr_ort < 75):
                        mak_harf = "CC"
                        mak_ort = 2.00
                    elif (mak_ogr_ort >= 65 or mak_ogr_ort < 70):
                        mak_harf = "DC"
                        mak_ort = 1.50
                    elif (mak_ogr_ort >= 60 or mak_ogr_ort < 65):
                        mak_harf = "DD"
                        mak_ort = 1.00
                    elif (mak_ogr_ort >= 50 or mak_ogr_ort < 60):
                        mak_harf = "FD"
                        mak_ort = 0.50
                    elif (mak_ogr_ort >= 0 or mak_ogr_ort < 50):
                        mak_harf = "FF"
                        mak_ort = 0.00
                    mak_ders_index += 1
                    makine.append([mak_ad, mak_ogr_ad, mak_ogr_no, mak_ogr_final, mak_ogr_vize, mak_ogr_ort, mak_harf, mak_ort])



    elif (bolum_secimi == 3):
        elk_ogr_index = 0
        elk_ders_index = 0
        elk_ders = input("Lütfen ders sayisini giriniz:")
        try:
            elk_ders = int(elk_ders)
        except ValueError:
            print("Lütfen bir sayi giriniz")
            continue
        elk_ogr = input("Lütfen toplam öğrenci sayısını giriniz:")
        try:
            elk_ogr = int(elk_ogr)
        except ValueError:
            print("Lütfen bir sayi giriniz")
            continue

        if (elk_ogr < 5 or elk_ogr > 20):
            print("Geçersiz bir büyüklük girdiniz.")
            continue
        else:
            for i in range(0, elk_ogr):
                elk_ogr_ad = input("Lütfen ogrenci adini giriniz:")
                elk_ogr_no = input("Lütfen ogrenci numarasini giriniz:")
                elk_ogr_index += 1
                for j in range(0, elk_ders):
                    elk_ad = input("Lütfen ders adini giriniz:")
                    elk_ogr_final = input("Lütfen final notunu giriniz:")
                    elk_ogr_vize = input("Lütfen vize notunu giriniz:")
                    try:
                        elk_ogr_final = float(elk_ogr_final)
                        elk_ogr_vize = float(elk_ogr_vize)
                    except ValueError:
                        print("Lütfen bir ondalık sayı veya sayı giriniz")
                        continue
                    elk_ogr_ort = (0.7 * elk_ogr_final) + (0.3 * elk_ogr_vize)

                    if (elk_ogr_ort < 0 or elk_ogr_ort > 100):
                        print("Hatalı bir ortalama hesaplandı")
                        break

                    if (elk_ogr_ort >= 90 or elk_ogr_ort <= 100):
                        elk_harf = "AA"
                        elk_ort = 4.00
                    elif (elk_ogr_ort >= 85 or elk_ogr_ort < 90):
                        elk_harf = "BA"
                        elk_ort = 3.50
                    elif (elk_ogr_ort >= 80 or elk_ogr_ort < 85):
                        elk_harf = "BB"
                        elk_ort = 3.00
                    elif (elk_ogr_ort >= 75 or elk_ogr_ort < 80):
                        elk_harf = "CB"
                        elk_ort = 2.50
                    elif (elk_ogr_ort >= 70 or elk_ogr_ort < 75):
                        elk_harf = "CC"
                        elk_ort = 2.00
                    elif (elk_ogr_ort >= 65 or elk_ogr_ort < 70):
                        elk_harf = "DC"
                        elk_ort = 1.50
                    elif (elk_ogr_ort >= 60 or elk_ogr_ort < 65):
                        elk_harf = "DD"
                        elk_ort = 1.00
                    elif (elk_ogr_ort >= 50 or elk_ogr_ort < 60):
                        elk_harf = "FD"
                        elk_ort = 0.50
                    elif (elk_ogr_ort >= 0 or elk_ogr_ort < 50):
                        elk_harf = "FF"
                        elk_ort = 0.00
                    elk_ders_index += 1
                    elektronik.append([elk_ad, elk_ogr_ad, elk_ogr_no, elk_ogr_final, elk_ogr_vize, elk_ogr_ort, elk_harf, elk_ort])
    elif (bolum_secimi == 4):
        print("""
        1-Öğrenci İşlemleri
        2-Ders İşlemleri
        3-Çıkış""")
        islem_secimi = input("Lütfen yapmak istediğiniz işlemi seçiniz:")
        try:
            islem_secimi = int(islem_secimi)
        except ValueError:
            print("Geçersiz seçim yaptınız.")
            continue

        if (islem_secimi == 1):
            print("""
            1-Öğrenci Adı
            2-Öğrenci No
            3-Öğrenci Notu
            4-Çıkış""")
            ogr_secim = input("Lütfen yapmak istediğiniz işlemi seçiniz:")
            try:
                ogr_secim = int(ogr_secim)
            except ValueError:
                print("Geçersiz seçim yaptınız.")
                continue

            if (ogr_secim == 4):
                print("Çıkış yapılıyor")
                break

            elif (ogr_secim == 1):
                print("""
                1-Bilgisayar
                2-Makine
                3-Elektronik
                4-Çıkış""")
                ogr_bolum = input("Lütfen ogrenci bolumunu giriniz")
                try:
                    ogr_bolum = int(ogr_bolum)
                except ValueError:
                    print("Geçersiz seçim yaptınız.")
                    continue

                if (ogr_bolum == 4):
                    print("Çıkış yapılıyor")
                    break

                elif (ogr_bolum == 1):
                    ogr_ad = input("Öğrenci adını giriniz:")
                    if (ogr_ad in bilgisayar):
                        yeni_ad = input("Yeni gireceğiniz adı giriniz:")
                        for ogr_ad in bilgisayar:
                            aranan_ad = bilgisayar.index(ogr_ad)

                            bilgisayar[aranan_ad][1] = yeni_ad
                    else:
                        print("Böyle bir isim bulunamadı")
                        print("Çıkış yapılıyor")
                        break

                elif (ogr_bolum == 2):
                    ogr_ad = input("Öğrenci adını giriniz:")
                    if (ogr_ad in makine):
                        yeni_ad = input("Yeni gireceğiniz adı giriniz:")
                        for ogr_ad in makine:
                            aranan_ad = makine.index(ogr_ad)
                            makine[aranan_ad][1] = yeni_ad
                    else:
                        print("Böyle bir isim bulunamadı")
                        print("Çıkış yapılıyor")
                        break
                elif (ogr_bolum == 3):
                    ogr_ad = input("Öğrenci adını giriniz:")
                    if (ogr_ad in elektronik):
                        yeni_ad = input("Yeni gireceğiniz adı giriniz:")
                        for ogr_ad in elektronik:
                            aranan_ad = elektronik.index(ogr_ad)
                            elektronik[aranan_ad][1] = yeni_ad
                    else:
                        print("Böyle bir isim bulunamadı")
                        print("Çıkış yapılıyor")
                        break
                else:
                    print("Geçersiz bir seçim yaptınız çıkış yapılıyor.")
                    break
            elif (ogr_secim == 2):
                print("""
                1-Bilgisayar
                2-Makine
                3-Elektronik
                4-Çıkış""")
                ogr_bolum = input("Lütfen ogrenci bolumunu giriniz")
                try:
                    ogr_bolum = int(ogr_bolum)
                except ValueError:
                    print("Geçersiz seçim yaptınız.")
                    continue
                if (ogr_bolum == 4):
                    print("Çıkış yapılıyor")
                    break
                elif (ogr_bolum == 1):
                    ogr_no = input("Öğrenci numarasını giriniz:")
                    if (ogr_no in bilgisayar):
                        yeni_no = input("Yeni gireceğiniz numarayı giriniz:")
                        for ogr_no in bilgisayar:
                            aranan_no = bilgisayar.index(ogr_no)
                            bilgisayar[aranan_no][1] = yeni_no
                    else:
                        print("Böyle bir numara bulunamadı")
                        print("Çıkış yapılıyor")
                        break

                elif (ogr_bolum == 2):
                    ogr_no = input("Öğrenci numarasını giriniz:")
                    if (ogr_no in makine):
                        yeni_no = input("Yeni gireceğiniz numarayı giriniz:")
                        for ogr_no in makine:
                            aranan_no = makine.index(ogr_no)
                            makine[aranan_no][1] = yeni_no
                    else:
                        print("Böyle bir numara bulunamadı")
                        print("Çıkış yapılıyor")
                        break

                elif (ogr_bolum == 3):
                    ogr_no = input("Öğrenci numarasını giriniz:")
                    if (ogr_no in elektronik):
                        yeni_no = input("Yeni gireceğiniz numarayı giriniz:")
                        for ogr_no in elektronik:
                            aranan_no = elektronik.index(ogr_no)
                            elektronik[aranan_no][1] = yeni_no

                    else:
                        print("Böyle bir numara bulunamadı")
                        print("Çıkış yapılıyor")
                        break
                else:
                    print("Geçersiz bir seçim yaptınız çıkış yapılıyor.")
                    break
            elif (ogr_secim == 3):
                print("""
                1-Bilgisayar
                2-Makine
                3-Elektronik
                4-Çıkış""")
                ogr_bolum = input("Lütfen ogrenci bolumunu giriniz")
                try:
                    ogr_bolum = int(ogr_bolum)
                except ValueError:
                    print("Geçersiz seçim yaptınız.")
                    continue
                if (ogr_bolum == 4):
                    print("Çıkış yapılıyor")
                    break
                elif (ogr_bolum == 1):
                    aranan = input("Lütfen ogrencinin adini veya no sunu giriniz")
                    aranan_ders = input("Lütfen ders adını giriniz")
                    ara_list = [aranan, aranan_ders]
                    if (aranan in bilgisayar):
                        yeni_not = input("Lütfen yeni vize notunu giriniz:")
                        yeni_not2 = input("Lütfen yeni final notunu giriniz:")

                        try:
                            yeni_not = float(yeni_not)
                            yeni_not2 = float(yeni_not2)
                        except ValueError:
                            print("Lütfen ondalıklı veya tam bir sayı giriniz")

                        yeni_ort = (yeni_not * 0.3) + (yeni_not2 * 0.7)
                        degisecek = bilgisayar.index(ara_list)
                        bilgisayar[degisecek]










    else:
        print("Geçersiz bir seçim yaptınız programdan çıkış yapılıyor")
        break
    break

