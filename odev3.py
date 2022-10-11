print("""
           1:OGRENCİ EKLEME
           2:OGRENCİ SİLME
           3:NOT GÜNCELLEME
           """)


secim1 = int(input("LUTFEN SEÇİMİNİZİ YAPINIZ"))
if secim1==1:
        print("""
                   1:BİLGİSAYAR MUHENDİSLİGİ
                   2:MEKATRONİK MUHENDİSLİGİ
                   3:MAKİNA MUHENDİSLİGİ
                   """)

        bolum_sec = int(input("HANGİ BOLUME OGRENCİ EKLEMEK İSTİYORSANIZ NUMARASINI SEÇİNİZ"))
        if bolum_sec == 1:

            print("BİLGİSAYAR MUHENDİSLİGİNE OGRENCİ EKLEME BOLUMU")

            ekle_ogr_saysı = int(input("eklemek istediğinş ogrenci adedi  giriniz"))
            ekle_ders_saysı = int(input("ders sayısını giriniz"))
            for x in range(ekle_ogr_saysı):
                gecici_list=[]
                ekle_ad = input("ogrenci adını giriniz")
                ekle_no = int(input("ogrenci no gr"))
                for h in range(ekle_ders_saysı):
                    eklenen_ders = input("DERS ADINI GİRİNİZ")
                    eklenen_vize = int(input("vize notlarını giriniz"))
                    eklenen_odev = int(input("odev notlrını giriniz"))
                    eklenen_final = int(input("final notlarını giriniz"))
                    eklenen_ort = eklenen_vize * 0.3 + eklenen_odev * 0.2 + eklenen_final * 0.5
                    if eklenen_ort < 0 or eklenen_ort > 100:
                        print("YANLIŞ ORTALAMA!!!")
                        break

                    if eklenen_ort >= 90 and eklenen_ort < 100:
                        durum = "AA"
                    elif eklenen_ort < 89 and eklenen_ort >= 85:
                        durum = "BA"
                    elif eklenen_ort >= 75 and eklenen_ort < 79:
                        durum = "CB"
                    elif eklenen_ort >= 70 and eklenen_ort < 74:
                        durum = "CC"
                    elif eklenen_ort >= 65 and eklenen_ort < 69:
                        durum = "DC"
                    elif eklenen_ort >= 60 and eklenen_ort < 64:
                        durum = "DD"
                    elif eklenen_ort >= 50 and eklenen_ort < 59:
                        durum = "FD"
                    else:
                        durum = "FF"
print(durum)
