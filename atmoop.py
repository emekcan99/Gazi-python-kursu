import random

class kullbil:
    def __init__(self,kullAdSoyad,sifre,bakiye,usdbakiye,borc):
        self.kullAdSoyad=kullAdSoyad
        self.sifre=sifre
        self.bakiye=bakiye
        self.usdbakiye=usdbakiye
        self.borc=borc


hesap1=kullbil("reçel tahin ersoğan","1453",128000,0,100)
hesap2=kullbil("mansur lavaş","0606",1000000,500000,0)
hesap3=kullbil("marul aksonar","1234",15000,5000,100000000000)
kulList=[hesap1,hesap2,hesap3]
bakiyeList=[hesap1.bakiye,hesap2.bakiye,hesap3.bakiye]

kart=hesap1

class ATM:
    def __init__(self,ad):
        self.ad=ad
        self.sifreKontrol()
        self.flag=True


    def sifreKontrol(self):
        hak=3
        for i in range(0,4):
            sifre=input("lütefen sifrenizi giriniz")
            if sifre==kart.sifre:
                self.prog()
            elif sifre!=kart.sifre or hak!=0:
                print("yanlış şifre girdiniz kalan hakkınız {}".format(hak))
                hak-=1
            if sifre!=kart.sifre and hak==-1:
                print("yanlış şifre girdiniz ve hakkınız kalmadı lütfen en yakın şubemize gidiniz")
                exit()






    def prog(self):
        secim=self.menu()
        if secim=="1":
            self.bakiyeKontrol()
        if secim=="2":
            self.borcKontrol()
        if secim=="3":
            self.borcOde()
        if secim=="4":
            self.paraCek()
        if secim=="5":
            self.paraYatir()
        if secim=="6":
            self.usdAl()
        if secim=="7":
            self.paraTransfer()
        if secim=="8":
            self.usdBakiyeKontrol()
        if secim=="9":
            self.geridon()
        if secim=="10":
            self.cikis()
    def menu(self):

        secim=input("""                           ------------------------------------
                    TCMB'ye hoş geldiniz sayın {}
                    lütfen yapmak istediğiniz işlemi seçiniz
                    1-bakiye kontrol    2-borç kontrol
                    3-borç öde          4-para çek
                    5-para yatır        6-usd al
                    7- para transfer et 8-usd bakiye kontrol
                    9-menu dön          10-çıkış
                    -------------------------------
                     """.format(kart.kullAdSoyad))
        return secim







    def bakiyeKontrol(self):
        bakiye=kart.bakiye
        print("bakiyeniz{}TL".format(bakiye))
        self.flag=False
        self.geridon()

    def borcKontrol(self):
        borc=kart.borc
        print("şuanki borcunuz {}TL".format(borc))
        self.flag=False
        self.geridon()
    def borcOde(self):
        a=input("nakit ödemek için 1 e bakiyeden ödemek için 2 ye basınız")
        if a=="1":
            miktar=int(input("lütfen ödemek istediğiniz miktarı giriniz"))
            if miktar>=kart.borc:
                kart.borc=0
                kart.bakiye=kart.bakiye+(miktar-kart.borc)
                print("borcunuz ödenmiştir kalan bakiye {}TL kalan borç {}TL".format(kart.bakiye,kart.borc))
                print("yatırdığınız miktar fazla olduğu için bakiyenize aktarılmıştır")
                self.geridon()
            elif miktar<kart.borc:
                kart.borc=kart.borc-miktar
                print("borcunuz ödenmiştir kalan bakiye {}TL kalan borç {}TL".format(kart.bakiye, kart.borc))
                self.geridon()
        elif a=="2":
            if kart.bakiye>=kart.borc:
                kart.bakiye=kart.bakiye-kart.borc
                kart.borc=0
                print("borcunuz ödenmiştir kalan bakiye {}TL kalan borç {}TL".format(kart.bakiye,kart.borc))
                self.geridon()
            elif kart.bakiye<kart.borc:
                kart.bakiye=0
                kart.borc=kart.borc-kart.bakiye
                print("borcunuz ödenmiştir kalan bakiye {} kalan borç {}".format(kart.bakiye, kart.borc))
                self.geridon()

    def paraCek(self):
        a=int(input("lütfen çekmek istediğiniz miktarı giriniz..."))
        if a>kart.bakiye:
            print("çekmek istediğiniz miktar bakiyenizde bulunmuyor...")
            self.geridon()
        elif a<0:
            print("negatif değer girilmez...")
            self.geridon()
        elif a<kart.bakiye:
            kart.bakiye=kart.bakiye-a
            print("işleminiz gerçekleşti yeni bakiyeniz{}".format(kart.bakiye))
            self.geridon()
    def paraYatir(self):
        b=int(input("lütfen yatırmak istediğiniz miktarı giriniz"))
        if b<0:
            print("negatif değer girilemez...")
            self.geridon()
        elif b>0:
            kart.bakiye=kart.bakiye+b
            print("para yatırma işlemi başarılı şuanki bakiyeniz {}TL".format(kart.bakiye))
            self.geridon()
    def usdAl(self):
        c=input("1-bakiyeden satın al 2-para yatırarak satın al")
        if c=="1":
            x=int(input("lütfen satın almak istediğiniz miktarı giriniz"))
            if kart.bakiye>=x:
                kart.bakiye=kart.bakiye-x
                kart.usdbakiye=random.random()
                print("usd bakiye {} tl bakiye {}".format(kart.usdbakiye,kart.bakiye))
                print("""
                AKIL SAĞLIĞINI KAYBET
                ░░░░▄▄▄▄▄▓▓▓▄▄▄░░░░░
                ░░░░▄▄▓▀▀▀▀▀▀▓▓▓▓▓▓▄░░░
                ░░▄▄▓▀▀░░░░░░░▒▒▒▒▒▀▓▄░
                ░▐▓▓▌░░░░░░░░░░░░▒▒▒▒▓▌
                ░▐▓▒░░▄▒▒▓▄▄▒▒▒░▒▄▄▄▒▒▓
                ░▓▓▌░░░░░▒▒▒▒▀▒▒▓▓▓▓▓▓▓
                ░▐▓░░░░▒▒▓(◐)▓░░░▒▓▓(◐)▒▓
                █░▀▄░█▄█▀▄▄░▀░▀▄▄▀░░█░█
                ░█░░░▀▄█▄█░█▀▄▄▄▄▄▀██░█
                ░░█░░░░█░███▄█▄█▄███░░█
                ░░░█░░░▀▀█░█▀█▀█▀███░█
                ░░░░▀▄░░░░▀▀▄█▄█▄█▄▀░█
                ░░░░░░▀▄▄░▒▒▒░░░░░░░░░█
                ░░░░░░░░░▀▀▄▄▄▄▄▄▄▄▄▄▀""")
                self.geridon()
            elif kart.bakiye<x:
                print("yetersiz bakiye")
                self.geridon()
        if c=="2":
            x = int(input("lütfen satın almak istediğiniz miktarı giriniz"))
            kart.usdbakiye=kart.usdbakiye+random.random()
            print("USD bakiye {}usd".format(kart.usdbakiye))
            print("""
            ZİHİNSEL SORUN
            ⣀⣠⣤⣤⣤⣤⢤⣤⣄⣀⣀⣀⣀⡀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
            ⠄⠉⠹⣾⣿⣛⣿⣿⣞⣿⣛⣺⣻⢾⣾⣿⣿⣿⣶⣶⣶⣄⡀⠄⠄⠄
            ⠄⠄⠠⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣆⠄⠄
            ⠄⠄⠘⠛⠛⠛⠛⠋⠿⣷⣿⣿⡿⣿⢿⠟⠟⠟⠻⠻⣿⣿⣿⣿⡀⠄
            ⠄⢀⠄⠄⠄⠄⠄⠄⠄⠄⢛⣿⣁⠄⠄⠒⠂⠄⠄⣀⣰⣿⣿⣿⣿⡀
            ⠄⠉⠛⠺⢶⣷⡶⠃⠄⠄⠨⣿⣿⡇⠄⡺⣾⣾⣾⣿⣿⣿⣿⣽⣿⣿
            ⠄⠄⠄⠄⠄⠛⠁⠄⠄⠄⢀⣿⣿⣧⡀⠄⠹⣿⣿⣿⣿⣿⡿⣿⣻⣿
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠛⠟⠇⢀⢰⣿⣿⣿⣏⠉⢿⣽⢿⡏
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠤⣤⣴⣾⣿⣿⣾⣿⣿⣦⠄⢹⡿⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⠒⣳⣶⣤⣤⣄⣀⣀⡈⣀⢁⢁⢁⣈⣄⢐⠃⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⣰⣿⣛⣻⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⣬⣽⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⢘⣿⣿⣻⣛⣿⡿⣟⣻⣿⣿⣿⣿⡟⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠛⢛⢿⣿⣿⣿⣿⣿⣿⣷⡿⠁⠄⠄⠄
            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠉⠉⠈⠄⠄⠄⠄⠄⠄""")
            self.geridon()
        else:
            print("hatalı giriş")
            self.geridon()
    def paraTransfer(self):
        a=int(input("lütfen göndermek istediğiniz hesap no sunu giriniz örn 1,2,3"))
        miktar=int(input("lütfen göndermek istediğiniz miktarı giriniz"))
        if miktar>kart.bakiye:
            print("göndermek istediğiniz miktar bakiyenizden yüksek")
            self.geridon()
        elif miktar<0:
            print("negatif değer gönderilemez")
            self.geridon()
        else:
            aHesap=bakiyeList[a]
            aHesap=aHesap+miktar
            kart.bakiye=kart.bakiye-miktar
            print("para transferi başarılı şuanki bakiyeniz {} gönderdiğiniz kişinin bakiyesi{}".format(kart.bakiye,aHesap))
            self.geridon()


    def usdBakiyeKontrol(self):
        print("şuanki bakiyeniz {}".format(kart.usdbakiye))
        self.geridon()
    def cikis(self):
        print("girdiğniz bilgiler kayıt ediliyor...")
        print("çıkış yapılıyor...")
        self.flag=False
        exit()

    def geridon(self):
        x=input("devam etmek için 9 a çıkış yapmak için 10 na basınız")
        if x=="9":
            self.prog()
        elif x=="10":
            self.cikis()

bank=ATM("Merkez Bankası")

while bank.flag:
    bank.prog()







