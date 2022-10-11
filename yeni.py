bilgisayar_muh = []

mekatronik_muh = []
makina_muh = []


def nott(vizee,odevv,finall):
    while True:
        ort = vizee * 0.3 + odevv * 0.2 + finall * 0.5

        if ort < 0 or ort > 100:
            print("YANLIŞ ORTALAMA!!!")
            break

        else:

            if ort >= 90 and ort <= 100:
                print(ort)
            elif ort < 90 and ort >= 85:
                print(ort)
            elif ort < 85 and ort >= 80:
                print(ort)
            elif ort >= 75 and ort < 80:
                print(ort)
            elif ort >= 70 and ort < 75:
                print(ort)
            elif ort >= 65 and ort < 70:
                print(ort)
            elif ort >= 60 and ort < 65:
                print(ort)
            elif ort >= 50 and ort < 60:
                print(ort)
            else:
                print(ort)
        return ort


def ortalama(vize, odev, final):
    while True:
        ort = vize * 0.3 + odev * 0.2 + final * 0.5

        if ort < 0 or ort > 100:
            print("YANLIŞ ORTALAMA!!!")
            break

        else:
            durumk = "kaldı"
            if ort >= 90 and ort <= 100:
                durumk = "AA"
            elif ort < 90 and ort >= 85:
                durumk = "BA"
            elif ort < 85 and ort >= 80:
                durumk = "BB"
            elif ort >= 75 and ort < 80:
                durumk = "CB"
            elif ort >= 70 and ort < 75:
                durumk = "CC"
            elif ort >= 65 and ort < 70:
                durumk = "DC"
            elif ort >= 60 and ort < 65:
                durumk = "DD"
            elif ort >= 50 and ort < 60:
                durumk = "FD"
            else:
                durumk = "FF"
        return durumk







def diger_işlem():
    while True:
        print("""
               1:OGRENCİ EKLEME
               2:OGRENCİ AD GUNCELLEME
               3:OGRENCİ NO GUNCELLEME
               4:OGRENCİ NOT GUNCELLEME
               5:ÇIKIŞ
               6:SİLME


               """)

        secim1 = int(input("LUTFEN SEÇİMİNİZİ YAPINIZ"))
        try:
            secim1 = int(secim1)
        except ValueError:
            print("RAKAM GİR")
            break
        if secim1 == 1:
            print("ÖGRENCİ EKLEME İŞLEMLERİ")
            print("""
                       1:BİLGİSAYAR MUHENDİSLİGİ
                       2:MEKATRONİK MUHENDİSLİGİ
                       3:MAKİNA MUHENDİSLİGİ
                       """)

            bolum_sec = int(input("HANGİ BOLUME OGRENCİ EKLEMEK İSTİYORSANIZ NUMARASINI SEÇİNİZ"))
            try:
                bolum_sec = int(bolum_sec)
            except ValueError:
                print("RAKAM GİR")
                break
            if bolum_sec == 1:

                print("BİLGİSAYAR MUHENDİSLİGİNE OGRENCİ EKLEME BOLUMU")

                ekle_ogr_saysı = int(input("eklemek istediğinş ogrenci adedi  giriniz"))
                try:
                    ekle_ogr_saysı = int(ekle_ogr_saysı)
                except ValueError:
                    print("RAKAM GİR")
                    break

                ekle_ders_saysı = int(input("ders sayısını giriniz"))
                try:
                    ekle_ders_saysı = int(ekle_ders_saysı)
                except ValueError:
                    print("RAKAM GİR")
                    break
                for x in range(ekle_ogr_saysı):
                    ekle_ad = input("ogrenci adını giriniz")
                    ekle_no = int(input("ogrenci no gr"))
                    for h in range(ekle_ders_saysı):
                        eklenen_ders = input("DERS ADINI GİRİNİZ")
                        eklenen_vize = int(input("vize notlarını giriniz"))
                        try:
                            eklenen_vize = int(eklenen_vize)
                        except ValueError:
                            print("RAKAM GİR")
                            break
                        eklenen_odev = int(input("odev notlrını giriniz"))
                        try:
                            eklenen_odev = int(eklenen_odev)
                        except ValueError:
                            print("RAKAM GİR")
                            break
                        eklenen_final = int(input("final notlarını giriniz"))
                        try:
                            eklenen_final = int(eklenen_final)
                        except ValueError:
                            print("RAKAM GİRİNİZ")
                            break
                        eklenen_ort = eklenen_vize * 0.3 + eklenen_odev * 0.2 + eklenen_final * 0.5
                        if eklenen_ort < 0 or eklenen_ort > 100:
                            print("YANLIŞ ORTALAMA!!!")
                            break
                        durum1 = "kaldı"

                        if eklenen_ort >= 90 and eklenen_ort < 100:
                            durum1 = "AA"
                        elif eklenen_ort < 89 and eklenen_ort >= 85:
                            durum1 = "BA"
                        elif eklenen_ort < 85 and eklenen_ort >= 80:
                            durum1 = "BB"
                        elif eklenen_ort >= 75 and eklenen_ort < 79:
                            durum1 = "CB"
                        elif eklenen_ort >= 70 and eklenen_ort < 74:
                            durum1 = "CC"
                        elif eklenen_ort >= 65 and eklenen_ort < 69:
                            durum1 = "DC"
                        elif eklenen_ort >= 60 and eklenen_ort < 64:
                            durum1 = "DD"
                        elif eklenen_ort >= 50 and eklenen_ort < 59:
                            durum1 = "FD"
                        else:
                            durum1 = "FF"
                        top_bil = [ekle_ad, ekle_no, eklenen_ders, eklenen_vize, eklenen_odev, eklenen_final,
                                   eklenen_ort, durum1]
                        bilgisayar_muh.append(top_bil)
                    print(bilgisayar_muh)
            elif bolum_sec == 2:
                print("MEKATRONİK MUHENDİSLİGİNE OGRENCİ EKLEME BOLUMU")

                mek_ekle_ogr_saysı = int(input("eklemek istediğinş ogrenci adedi  giriniz"))
                mek_ekle_ders_saysı = int(input("ders sayısını giriniz"))
                for y in range(0, mek_ekle_ogr_saysı):
                    mek_ekle_ad = input("ogrenci adını giriniz")
                    mek_ekle_no = int(input("ogrenci no gr"))
                    for o in range(0, mek_ekle_ders_saysı):
                        mek_eklenen_ders = input("DERS ADINI GİRİNİZ")
                        mek_eklenen_vize = int(input("vize notlarını giriniz"))
                        mek_eklenen_odev = int(input("odev notlrını giriniz"))
                        mek_eklenen_final = int(input("final notlarını giriniz"))
                        mek_eklenen_ort = mek_eklenen_vize * 0.3 + mek_eklenen_odev * 0.2 + mek_eklenen_final * 0.5
                        if mek_eklenen_ort < 0 or mek_eklenen_ort > 100:
                            print("YANLIŞ ORTALAMA!!!")
                            break

                        else:
                            durum2 = "kaldı"
                            if mek_eklenen_ort >= 90 and mek_eklenen_ort < 100:
                                durum2 = "AA"
                            elif mek_eklenen_ort < 89 and mek_eklenen_ort >= 85:
                                durum2 = "BA"
                            elif mek_eklenen_ort < 85 and mek_eklenen_ort >= 80:
                                durum2 = "BB"
                            elif mek_eklenen_ort >= 75 and mek_eklenen_ort < 79:
                                durum2 = "CB"
                            elif mek_eklenen_ort >= 70 and mek_eklenen_ort < 74:
                                durum2 = "CC"
                            elif mek_eklenen_ort >= 65 and mek_eklenen_ort < 69:
                                durum2 = "DC"
                            elif mek_eklenen_ort >= 60 and mek_eklenen_ort < 64:
                                durum2 = "DD"
                            elif mek_eklenen_ort >= 50 and mek_eklenen_ort < 59:
                                durum2 = "FD"
                            else:
                                durum2 = "FF"

                            top_mek = [mek_ekle_ad, mek_ekle_no, mek_eklenen_ders, mek_eklenen_vize, mek_eklenen_odev,
                                       mek_eklenen_final, mek_eklenen_ort, durum2]
                            mekatronik_muh.append(top_mek)
                    print(mekatronik_muh)
            else:
                print("MAKİNA MUHENDİSLİGİNE OGRENCİ EKLEME BOLUMU")

                mak_ekle_ogr_saysı = int(input("eklemek istediğinş ogrenci adedi  giriniz"))
                mak_ekle_ders_saysı = int(input("ders sayısını giriniz"))
                for s in range(0, mak_ekle_ogr_saysı):
                    mak_ekle_ad = input("ogrenci adını giriniz")
                    mak_ekle_no = int(input("ogrenci no gr"))
                    for v in range(0, mak_ekle_ders_saysı):
                        mak_eklenen_ders = input("DERS ADINI GİRİNİZ")
                        mak_eklenen_vize = int(input("vize notlarını giriniz"))
                        mak_eklenen_odev = int(input("odev notlrını giriniz"))
                        mak_eklenen_final = int(input("final notlarını giriniz"))
                        mak_eklenen_ort = mak_eklenen_vize * 0.3 + mak_eklenen_odev * 0.2 + mak_eklenen_final * 0.5
                        if mak_eklenen_ort < 0 or mak_eklenen_ort > 100:
                            print("YANLIŞ ORTALAMA!!!")
                            break
                        else:

                            durum3 = "kaldı"
                            if mak_eklenen_ort >= 90 and mak_eklenen_ort < 100:
                                durum3 = "AA"
                            elif mak_eklenen_ort < 89 and mak_eklenen_ort >= 85:
                                durum3 = "BA"
                            elif mak_eklenen_ort < 85 and mak_eklenen_ort >= 79:
                                durum3 = "BB"
                            elif mak_eklenen_ort >= 75 and mak_eklenen_ort < 79:
                                durum3 = "CB"
                            elif mak_eklenen_ort >= 70 and mak_eklenen_ort < 74:
                                durum3 = "CC"
                            elif mak_eklenen_ort >= 65 and mak_eklenen_ort < 69:
                                durum3 = "DC"
                            elif mak_eklenen_ort >= 60 and mak_eklenen_ort < 64:
                                durum3 = "DD"
                            elif mak_eklenen_ort >= 50 and mak_eklenen_ort < 59:
                                durum3 = "FD"
                            else:
                                durum3 = "FF"
                            top_mak = [mak_ekle_ad, mak_ekle_no, mak_eklenen_ders, mak_eklenen_vize, mak_eklenen_odev,
                                       mak_eklenen_final, mak_eklenen_ort, durum3]
                            makina_muh.append(top_mak)
                    print(makina_muh)
        elif secim1 == 2:
            print("OGRENCİ AD GÜNCELLEME İŞLEMLERİ")
            print("""
            1:BİLGİSAYAR MUHENDİSLİGİ
            2:MEKATRONİK MUHENDİSLİĞİ
            3:MAKİNA MUHENDİSLİĞİ
            """)
            ad_degisim = int(input("HANGİ BOLUMDEKİ OGRENCİNİN ADINI DEGİSTİRMEK İSTİYORSUNUZ SEÇİNİZ"))
            if ad_degisim == 1:
                print("BİLGİSAYAR MUHENDİSLİGİ OGRENCİ İSİMLERİ DEĞİŞTİRME  BOLUMU")
                adı = input("DEĞİŞTİRMEK İSTEDİĞİNİZ İSMİ GİRİNİZ")
                yeni_ad = input("YENİ İSİM GİRİNİZ")
                index = 0
                for v in bilgisayar_muh:
                    if adı in v:
                        bilgisayar_muh[index][0] = yeni_ad
                    index += 1



                print(bilgisayar_muh)
            elif ad_degisim == 2:
                print("MEKATRONİK MUHENDİSLİGİ OGRENCİ İSİMLERİ DEĞİŞTİRME BOLUMU")
                adı1 = input("DEĞİŞTİRMEK İSTEDİĞİNİZ İSMİ GİRİNİZ")
                yeni_ad1 = input("YENİ İSİM GİRİNİZ")
                index1 = 0
                for h in mekatronik_muh:
                    if adı1 in h:
                        mekatronik_muh[index1][0] = yeni_ad1
                    index1 = index1 + 1


                print(mekatronik_muh)


            else:
                print("MAKİNA MUHENDİSLİGİ OGRENCİ İSİMLERİ BOLUMU")
                adı3 = input("DEĞİŞTİRMEK İSTEDİĞİNİZ İSMİ GİRİNİZ")
                yeni_isim2 = input("YENİ İSMİ GİRİNİZ")
                index3 = 0
                for mkn_el in makina_muh:

                    if adı3 in mkn_el:
                        makina_muh[index3][0] = yeni_isim2
                    index3 += 1

                print(makina_muh)
        elif secim1 == 3:
            print("OGRENCİ NO GUNCELLEME İŞLEMLERİ")
            print("""
                       1:BİLGİSAYAR MUHENDİSLİGİ
                       2:MEKATRONİK MUHENDİSLİĞİ
                       3:MAKİNA MUHENDİSLİĞİ
                       """)
            no_sec = int(input("HANGİ BOLUMUN OGRENCİSİNİN NUMARASINI DEGİŞTİRMEK İSTİYORSANIZ NUMARASINI SEÇİNİZ"))
            if no_sec == 1:
                print("BİLGİSAYAR MUHENDİSLİGİ OGRENCİ NUMARALARI DEĞİŞTİRME BOLUMU")
                degis_no = int(input("DEĞİŞECEK NUMARAYI GİRİNİZ"))
                yni_no = int(input("YENİ NUMARAYI GİRİNİZ"))
                indexk = 0
                for ind in bilgisayar_muh:
                    if degis_no in ind:
                        bilgisayar_muh[indexk][1] = yni_no

                    indexk = indexk + 1


                print(bilgisayar_muh)
            elif no_sec == 2:
                print("MEKATRONİK MUHENDİSLİGİ OGRENCİ NUMARALARI DEĞİŞTİRME BOLUMU")
                degis_no1 = int(input("DEĞİŞECEK NUMARAYI GİRİNİZ"))
                yeni_no = int(input("YENİ NUMARAYI GİRİNİZ"))
                index_meka = 0
                for no_m in mekatronik_muh:

                    if degis_no1 in no_m:
                        mekatronik_muh[index_meka][1] = yeni_no
                    index_meka = index_meka + 1


                print(mekatronik_muh)
            else:
                print("MAKİNA MUHENDİSLİGİ OGRENCİ NUMARALARI")
                degis_no2 = int(input("DEĞİŞECEK NUMARAYI GİRİNİZ"))
                yeni_no_makina = int(input("YENİ NUMARAYI GİRİNİZ"))
                index_mak = 0
                for h in makina_muh:
                    if degis_no2 in h:
                        makina_muh[index_mak][1] = yeni_no_makina
                    index_mak = index_mak + 1


                print(makina_muh)
        elif secim1 == 4:
            print("NOT GUNCELLEME İŞLEMLERİ")
            print("""""
            1:BİLGİSAYAR MUHENDİSLİGİ
            2:MEKATRONİK MUHENDİSLİGİ
            3:MAKİNA MUHENDİSLİGİ
            4:ÇIKIŞ
            """)
            bol_sec = int(input("HANGİ BOLUMUN OGRENCİLERİNİN NOTUNU DEĞİŞTİRMEK İSTİYORSANIZ NUMARASINI SEÇİNİZ"))
            if bol_sec == 1:
                print("BİLGİSAYAR MUHENDİSLİGİ NOT DEĞİŞTİRME BOLUMU")
                print(""""
                1:VİZE
                2:ODEV
                3:FİNAL """)
                sınav_sec = int(input("HANGİ NOTUNU DEĞİŞTİRMEK İSTİYORSAN NUMARASINI SEÇ"))
                if sınav_sec == 1:
                    print(" BİLGİSAYAR MUHENDİSLİĞİ VİZE DEĞİŞTİRME")
                    gir_vize = int(input("DEĞİŞTİRMEK İSTEDİĞİNİZ VİZEYİ GİRİNİZ"))
                    yeni_vize = int(input("OGRENCİNİN YENİ NOTUNU GİRİNİZ"))
                    index_bil = 0
                    for l in bilgisayar_muh:
                        if gir_vize in l:
                            bilgisayar_muh[index_bil][3] = yeni_vize
                            bilgisayar_muh[index_bil][7]=ortalama(yeni_vize,bilgisayar_muh[index_bil][4],bilgisayar_muh[index_bil][5])
                            bilgisayar_muh[index_bil][6]=nott(yeni_vize,bilgisayar_muh[index_bil][4],bilgisayar_muh[index_bil][5])
                            index_bil += 1

                        else:
                            print("GİRİLEN VİZEYE AİT OGRENCİ YOK")
                            break


                    print(bilgisayar_muh)



                elif sınav_sec == 2:
                    print(" BİLGİSAYAR MUHENDİSLİĞİ ODEV DEĞİŞTİRME")
                    gir_odev = int(input("DEĞİŞTİRMEK İSTEDİĞİNİZ ODEVİ GİRİNİZ"))
                    yeni_odev = int(input("OGRENCİNİN YENİ NOTUNU GİRİNİZ"))
                    index_bil_odev = 0
                    for d in bilgisayar_muh:
                        if gir_odev in d:
                            bilgisayar_muh[index_bil_odev][4] = yeni_odev

                            bilgisayar_muh[index_bil_odev][7]=ortalama(bilgisayar_muh[index_bil_odev][3],yeni_odev,bilgisayar_muh[index_bil_odev][5])
                            bilgisayar_muh[index_bil_odev][6]=nott(bilgisayar_muh[index_bil_odev][3],yeni_odev,bilgisayar_muh[index_bil_odev][5])
                            index_bil_odev += 1

                        else:
                            print("GİRİLEN ODEVE AİT OGRENCİ YOK")
                            break
                    print(bilgisayar_muh)
                else:
                    print(" BİLGİSAYAR MUHENDİSLİĞİ FİNAL DEĞİŞTİRME")
                    gir_final = int(input("DEĞİŞTİRMEK İSTEDİĞİNİZ FİNALİ GİRİNİZ"))
                    yeni_final = int(input("OGRENCİNİN YENİ NOTUNU GİRİNİZ"))
                    index_bil_final = 0
                    for eleman_bill in bilgisayar_muh:
                        if gir_final in eleman_bill:
                            bilgisayar_muh[index_bil_final][5] = yeni_final
                            bilgisayar_muh[index_bil_final][7]=ortalama(bilgisayar_muh[index_bil_final][3],bilgisayar_muh[index_bil_final][4],yeni_final)
                            bilgisayar_muh[index_bil_final][6]=nott(bilgisayar_muh[index_bil_final][3],bilgisayar_muh[index_bil_final][4],yeni_final)
                            index_bil_final += 1

                        else:
                            print("GİRİLEN FİNALE AİT OGRENCİ YOK")
                            break
                    print(bilgisayar_muh)
            elif bol_sec == 2:

                print(" MEKATRONİK MUHENDİSLİGİ NOT DEĞİŞTİRME BOLUMU")
                print(""""
                1:VİZE
                2:ODEV
                3:FİNAL """)
                sınav_sec1 = int(input("HANGİ NOTUNU DEĞİŞTİRMEK İSTİYORSAN NUMARASINI SEÇ"))
                if sınav_sec1 == 1:
                    print(" MEKATRONİK MUHENDİSLİĞİ VİZE DEĞİŞTİRME")
                    gir_vize1 = int(input("DEĞİŞTİRMEK İSTEDİĞİNİZ VİZEYİ GİRİNİZ"))
                    yeni_vize1 = int(input("OGRENCİNİN YENİ NOTUNU GİRİNİZ"))
                    index_mek1 = 0
                    for l in mekatronik_muh:
                        if gir_vize1 in l:
                            mekatronik_muh[index_mek1][3] = yeni_vize1
                            mekatronik_muh[index_mek1][7]=ortalama(yeni_vize1, mekatronik_muh[index_mek1][4], mekatronik_muh[index_mek1][5])
                            mekatronik_muh[index_mek1][6]=nott(yeni_vize1,mekatronik_muh[index_mek1][4],mekatronik_muh[index_mek1][5])
                            index_mek1 += 1

                elif sınav_sec1 == 2:
                    print(" MEKATRONİK MUHENDİSLİĞİ ODEV DEĞİŞTİRME")
                    gir_odev2 = float(input("DEĞİŞTİRMEK İSTEDİĞİNİZ ODEVİ GİRİNİZ"))
                    yeni_odev2 = float(input("OGRENCİNİN YENİ NOTUNU GİRİNİZ"))
                    index_mek_odev = 0
                    for d in mekatronik_muh:
                        if gir_odev2 in d:
                            mekatronik_muh[index_mek_odev][4] = yeni_odev2
                            mekatronik_muh[index_mek_odev][7] = ortalama(mekatronik_muh[index_mek_odev][3], yeni_odev2, mekatronik_muh[index_mek_odev][5])
                            mekatronik_muh[index_mek_odev][6] = nott(mekatronik_muh[index_mek_odev][3], yeni_odev2, mekatronik_muh[index_mek_odev][5])
                            index_mek_odev += 1

                        else:
                            print("GİRİLEN ODEVE AİT OGRENCİ YOK")
                            break
                    print(mekatronik_muh)
                else:
                    print(" MEKATRONİK MUHENDİSLİĞİ FİNAL DEĞİŞTİRME")
                    gir_final3 = float(input("DEĞİŞTİRMEK İSTEDİĞİNİZ FİNALİ GİRİNİZ"))
                    yeni_final3 = float(input("OGRENCİNİN YENİ NOTUNU GİRİNİZ"))
                    index_meek_final = 0
                    for eleman_meka in mekatronik_muh:
                        if gir_final3 in eleman_meka:
                            mekatronik_muh[index_meek_final][5] = yeni_final3
                            mekatronik_muh[index_meek_final][7]=ortalama(mekatronik_muh[index_meek_final][3],mekatronik_muh[index_meek_final][4],yeni_final3)
                            mekatronik_muh[index_meek_final][6]=nott(mekatronik_muh[index_meek_final][3],mekatronik_muh[index_meek_final][4],yeni_final3)
                            index_meek_final += 1

                        else:
                            print("GİRİLEN FİNALE AİT OGRENCİ YOK")
                            break
                    print(mekatronik_muh)
            elif bol_sec == 3:

                print(" MAKİNA MUHENDİSLİGİ NOT DEĞİŞTİRME BOLUMU")
                print(""""
                1:VİZE
                2:ODEV
                3:FİNAL """)
                sınav_sec_33 = int(input("HANGİ NOTUNU DEĞİŞTİRMEK İSTİYORSAN NUMARASINI SEÇ"))
                if sınav_sec_33 == 1:
                    print(" MAKİNA MUHENDİSLİĞİ VİZE DEĞİŞTİRME")
                    gir_vize49 = int(input("DEĞİŞTİRMEK İSTEDİĞİNİZ VİZEYİ GİRİNİZ"))
                    yeni_vize49 = int(input("OGRENCİNİN YENİ NOTUNU GİRİNİZ"))
                    index_makina44 = 0
                    for eleman in makina_muh:
                        if gir_vize49 in eleman:
                            makina_muh[index_makina44][3] = yeni_vize49
                            makina_muh[index_makina44][7]=ortalama(yeni_vize49,makina_muh[index_makina44][4],makina_muh[index_makina44][5])
                            makina_muh[index_makina44][6]=nott(yeni_vize49,makina_muh[index_makina44][4],makina_muh[index_makina44][5])

                            index_makina44 += 1
                        else:
                            print("GİRİLEN VİZEYE AİT OGRENCİ YOK")
                            break
                    print(makina_muh)
                elif sınav_sec_33 == 2:
                    print(" MAKİNA MUHENDİSLİĞİ ODEV DEĞİŞTİRME")
                    gir_odev50 = int(input("DEĞİŞTİRMEK İSTEDİĞİNİZ ÖDEVİ GİRİNİZ"))
                    yeni_odev50 = int(input("OGRENCİNİN YENİ NOTUNU GİRİNİZ"))
                    index_makina50 = 0
                    for eleman_makina in makina_muh:
                        if gir_odev50 in eleman_makina:
                            makina_muh[index_makina50][4] = yeni_odev50
                            makina_muh[index_makina50][7]=ortalama(makina_muh[index_makina50][3],yeni_odev50,makina_muh[index_makina50][5])
                            makina_muh[index_makina50][6]=nott(makina_muh[index_makina50][3],yeni_odev50,makina_muh[index_makina50][5])
                            index_makina50 += 1


                        else:
                            print("GİRİLEN ODEVE AİT OGRENCİ YOK")
                            break
                    print(makina_muh)
                else:
                    print(" MAKİNA MUHENDİSLİĞİ FİNAL DEĞİŞTİRME")

                    gir_final00 = int(input("DEĞİŞTİRMEK İSTEDİĞİNİZ FİNALİ GİRİNİZ"))
                    yeni_final00 = int(input("OGRENCİNİN YENİ NOTUNU GİRİNİZ"))
                    index_makina00 = 0
                    for eleman_makina0 in makina_muh:
                        if gir_final00 in eleman_makina0:
                            makina_muh[index_makina00][5] = yeni_final00
                            makina_muh[index_makina00][7]=ortalama(makina_muh[index_makina00][3],makina_muh[index_makina00][4],yeni_final00)
                            makina_muh[index_makina00][6]=nott(makina_muh[index_makina00][3],makina_muh[index_makina00][4],yeni_final00)
                            index_makina00 += 1



                        else:
                            print("GİRİLEN FİNALE AİT OGRENCİ YOK")
                            break
                    print(makina_muh)
            else:
                print("ÇIKIŞ YAPILIYOR")
                break
        elif secim1 == 5:
            print("ÇIKIŞ YAPILIYOR")
            break
        else:
            print(""""
            1:BİLGİSAYR MUHENDİSLİĞİ
            2:MEKATRONİK MUHENDİSLİĞİ
            3:MAKİNA MUHENDİSLİĞİ""")
            bolum_secc = int(input("BOLUM SEÇİNİZ"))
            if bolum_secc == 1:
                isim = input("silinecek ismi gir")
                index = 0
                for i in bilgisayar_muh:
                    if isim in i:
                        bilgisayar_muh.pop([index][0])
                    index = index + 1
                print(bilgisayar_muh)
            elif bolum_secc == 2:
                isim1 = input("silinecek ismi gir")
                indexx = 0
                for eleman in mekatronik_muh:
                    if isim1 in eleman:
                        mekatronik_muh.pop(indexx)
                    indexx = indexx + 1
                print(mekatronik_muh)
            else:
                isim2 = input("silinecek isimi gir")
                indexxx = 0
                for eleman2 in makina_muh:
                    if isim2 in eleman2:
                        makina_muh.pop(indexxx)
                    indexxx = indexxx + 1
                print(makina_muh)






print("""
   1:BİLGİSAYAR MUHENDİSLİGİ
   2:MEKATRONİK MUHENDİSLİĞİ
   3:MAKİNA MUHENDİSLİĞİ
   4:DİĞER İŞLEMLER(ÖĞRENCİ ARAMA VS)
   5:ÇIKIŞ
   """)
while True:

    secim = input("lutfen bir secim yapınız")
    try:
        secim = int(secim)
    except ValueError:
        print("****LUTFEN 1-5 ARASI RAKAM SEÇİNİZ")

    if secim == 1:
        print("BİLGİSAYAR MUHENDİSLİĞİ SEÇTİNİZ")
        blgsyr_ogrnc_sayı = int(input("ogrenci sayısıı giriniz.5 ile 20 arasında olmalıdır"))
        bilgsyr_ders_sayısı = int(input("kac ders gireceğinizi yazınız"))
        if blgsyr_ogrnc_sayı < 5 or blgsyr_ogrnc_sayı > 20:
            print("OGRENCİ SAYISI 5 İLE 20 ARASINDA OLMALIDR")
            continue
        else:

            for i in range(blgsyr_ogrnc_sayı):
                bil_ogr_ad = input("ogrenci adını giriniz")
                bil_ogr_no = int(input("ogrenci no gir"))

                for k in range(bilgsyr_ders_sayısı):

                    ders_adı = input("LUTFEN DERS ADINI GİRİNİZ")
                    bil_ogr_vize = int(input("vize notlarını giriniz"))

                    bil_ogr_odev = int(input("odev notunu giriniz"))
                    bil_ogr_final = int(input("final notlarını giriniz"))

                    ortalama7 = bil_ogr_vize * 0.3 + bil_ogr_odev * 0.2 + bil_ogr_final * 0.5

                    if ortalama7 < 0 or ortalama7 > 100:
                        print("YANLIŞ ORTALAMA!!!")
                        break

                    else:
                        durum5 = "kaldı"
                        if ortalama7 >= 90 and ortalama7 <= 100:
                            durum5 = "AA"
                        elif ortalama7 < 90 and ortalama7 >= 85:
                            durum5 = "BA"
                        elif ortalama7 < 85 and ortalama7 >= 80:
                            durum5 = "BB"
                        elif ortalama7 >= 75 and ortalama7 < 80:
                            durum5 = "CB"
                        elif ortalama7 >= 70 and ortalama7 < 75:
                            durum5 = "CC"
                        elif ortalama7 >= 65 and ortalama7 < 70:
                            durum5 = "DC"
                        elif ortalama7 >= 60 and ortalama7 < 65:
                            durum5 = "DD"
                        elif ortalama7 >= 50 and ortalama7 < 60:
                            durum5 = "FD"
                        else:
                            durum5 = "FF"
                        toplam_bil = [bil_ogr_ad, bil_ogr_no, ders_adı, bil_ogr_vize, bil_ogr_odev, bil_ogr_final,
                                      ortalama7, durum5]
                        bilgisayar_muh.append(toplam_bil)
            print(bilgisayar_muh)
    elif secim == 2:
        print("MEKATRONİK MUHENDİSLİĞİ SEÇTİNİZ")
        mekat_ogr_sayısı = int(input("ogrenci sayısı giriniz"))
        mekat_ders_sayısı = int(input("ders sayısını giriniz"))
        if mekat_ogr_sayısı < 5 or mekat_ogr_sayısı > 20:
            print("DERS SAYSI 5 İLE 20 ARASINDA OLMALIDIR")
            continue
        else:

            for c in range(mekat_ogr_sayısı):
                ad = input("ogrenci adını giriniz")
                no = int(input("ogrenci numarasını giriniz"))
                for p in range(mekat_ders_sayısı):
                    meka_ders_adı = input("ders adını giriniz")
                    meka_vize = float(input("vize notunu giriniz"))
                    meka_odev = float(input("odev notunun giriniz"))
                    meka_final = float(input("final notunu giriniz"))
                    ortalama = meka_vize * 0.3 + meka_odev * 0.2 + meka_final * 0.5
                    durum = "kaldı"
                    if ortalama < 0 or ortalama > 100:
                        print("YANLIŞ ORTALAMA!!!")
                        break

                    else:
                        durum5 = "kaldı"
                        if ortalama >= 90 and ortalama <= 100:
                            durum5 = "AA"
                        elif ortalama <= 89 and ortalama >= 85:
                            durum5 = "BA"
                        elif ortalama <= 84 and ortalama >= 80:
                            durum5 = "BB"

                        elif ortalama >= 75 and ortalama <= 79:
                            durum5 = "CB"
                        elif ortalama >= 70 and ortalama <= 74:
                            durum5 = "CC"
                        elif ortalama >= 65 and ortalama <= 69:
                            durum5 = "DC"
                        elif ortalama >= 60 and ortalama <= 64:
                            durum5 = "DD"
                        elif ortalama >= 50 and ortalama <= 59:
                            durum5 = "FD"
                        else:
                            durum5 = "FF"

                        toplam_mek = [ad, no, meka_ders_adı, meka_vize, meka_odev, meka_final, ortalama, durum5]
                        mekatronik_muh.append(toplam_mek)
            print(mekatronik_muh)
    elif secim == 3:
        print("MAKİNA MUHENDİSLİĞİ SEÇTİNİZ")
        makn_ogr_says = int(input("lutfen ogrenci sayısını giriniz"))
        makn_ders_says = int(input("ders sayısını giriniz"))
        if makn_ogr_says < 5 or makn_ogr_says > 20:
            print("OGRENCİ SAYISI 5 İLE 20 ARASINDA OLMALIDIR")
            continue
        else:
            for m in range(makn_ogr_says):
                mkna_ad = input("ogrenci adını giriniz")
                mkna_no = int(input("ogrenci no giriniz"))
                for n in range(makn_ders_says):
                    mkn_ders = input("DERS ADINI GİRİNİZ")
                    mkn_vize = int(input("vize notlarını giriniz"))
                    mkn_odev = int(input("odev notlrını giriniz"))
                    mkn_final = int(input("final notlarını giriniz"))
                    mkn_ort = mkn_vize * 0.3 + mkn_odev * 0.2 + mkn_final * 0.5
                    if mkn_ort < 0 or mkn_ort > 100:
                        print("YANLIŞ ORTALAMA!!!")
                        break

                    else:
                        durum4 = "kaldı"
                        if mkn_ort >= 90 and mkn_ort < 100:
                            durum4 = "AA"
                        elif mkn_ort <= 89 and mkn_ort >= 85:
                            durum4 = "BA"
                        elif mkn_ort >= 80 and mkn_ort <= 84:
                            durum4 = "BB"
                        elif mkn_ort >= 75 and mkn_ort < 79:
                            durum4 = "CB"
                        elif mkn_ort >= 70 and mkn_ort < 74:
                            durum4 = "CC"
                        elif mkn_ort >= 65 and mkn_ort < 69:
                            durum4 = "DC"
                        elif mkn_ort >= 60 and mkn_ort < 64:
                            durum4 = "DD"
                        elif mkn_ort >= 50 and mkn_ort < 59:
                            durum4 = "FD"
                        else:
                            durum4 = "FF"

                        toplam_makina = [mkna_ad, mkna_no, mkn_ders, mkn_vize, mkn_odev, mkn_final, mkn_ort, durum4]
                        makina_muh.append(toplam_makina)
            print(makina_muh)
    elif secim == 4:
        print("DİGER İŞLEMLERİ SEÇTİNİZ")
        diger_işlem()
    else:

        print("ÇIKIŞ YAPILIYOR")
        break
























