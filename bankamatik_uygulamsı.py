hesap_emre={
    "ad":"emre","soyad":"almamıs","bakiye":1000,"ek_bakiye":2000
    }

hesap_suna={
    "ad":"suna","soyad":"almamıs","bakiye":1500,"ek_bakiye":1200
}

def para_cekme(hesap):
    print(f"merhaba {hesap['ad']}")
    miktar=int(input("cekmek istediğiniz tutarı giriniz "))

    if(hesap['bakiye'] > miktar):
        hesap['bakiye']=hesap['bakiye']-miktar
        print(f"{miktar} tutarındaki paranızı alabirsiniz")
        kaln_bakiye(hesap)

    else:

        toplam = hesap['bakiye']+hesap['ek_bakiye']

        if(toplam > miktar):
            ek_kullanım=input("ek hesap kullanmı istermisniz (e/h) ")
            if(ek_kullanım=="e"):
                ek_kullanılacak_miktar=miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ek_bakiye']=hesap['ek_bakiye']-ek_kullanılacak_miktar
                print("paranızı alabirsiniz.")
                kaln_bakiye(hesap)
            else:
               kaln_bakiye(hesap)
        else:
                print("bakiyeniz yetersizdir")

def kaln_bakiye(hesap):
    print( f"kalan bakiyeniz :{hesap['bakiye']}  ek hesap bakiyeniz ise:{hesap['ek_bakiye']}")

para_cekme(hesap_emre)
para_cekme(hesap_emre)


