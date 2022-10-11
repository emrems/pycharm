class Ucus():

    havayolu="THY"
    def __init__(self,kod,kalkis,varis,gecen_sure,kapasite,yolcu):

        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.gecen_sure=gecen_sure
        self.kapasite=kapasite
        self.yolcu=yolcu
        self.anons()
        self.bilet_satis()

    def anons(self):
        return print("{} kodlu {}-{} uçağımız {} dakika içinde {} da olacaktır".format(self.kod,self.kalkis,self.varis,self.gecen_sure,self.varis))
    def kalan_koltuk(self):
        return self.kapasite - self.yolcu

    def bilet_satis(self,bilet_adedi=1):
        if((self.yolcu+bilet_adedi)<self.kapasite):
            self.yolcu+=bilet_adedi
            self.kalan_koltuk()
            print("{} adet bilet satılmıştır.Kalan koltuk {} ".format(bilet_adedi,self.kalan_koltuk()))
        else:
            print("yer kalmamıştır")

    def bilet_iptal(self,iptal_edilen_kltk=1):

        if(self.yolcu>iptal_edilen_kltk):
            self.yolcu -= iptal_edilen_kltk
            print("{} adet bilet iptal edilmiştir.Güncel kalan koltuk saysı {} ".format(iptal_edilen_kltk,self.kalan_koltuk()))
        else:
            print("iptal işlemi gerçekleştirilemedi")




ucus1=Ucus("md32","muş","kocaeli",24,340,200)

