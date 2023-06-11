class Musteri:
    def __init__(self, ad, soyad, kartsifre, hesapbakiye, kredikartborc, sonodeme):
        self.ad = ad
        self.kartsifre = kartsifre
        self.soyad = soyad
        self.hesapbakiye = hesapbakiye
        self.kredikartborc = kredikartborc
        self.sonodeme = sonodeme


AhmetHesap = Musteri("Ahmet", "candan", "1357", 5000, 4200, "20/11/2022")
MehmetHesap = Musteri("Mehmet", "candan", "2468", 6000, 3800, "28/11/2022")
TakilanKart = AhmetHesap


class ATM:
    def __init__(self, atmAd):
        self.atmad = atmAd
        self.girisKontrol()
        self.dongu = True

    def girisKontrol(self):
        Hak = 2
        for i in range(1, 3):
            Sifre = input("\nLütfen 4 haneli şifrenizi giriniz:")
            if Sifre == TakilanKart.kartsifre:
                self.Program()
            elif Sifre != TakilanKart.kartsifre and Hak != 0:
                print("Hatalı Şifre Girdiniz.Kalan Hakkınız {} ".format(Hak))
                Hak -= 1
            elif Sifre != TakilanKart.kartsifre and Hak == 0:
                print("""şifrenizi 3 Defa Hatalı Girdiğinizden Dolayı 
                kartınız Bloke Olmuştur.Lütfen En yakın Şubesmize Başvurunuz!!!""")
                exit()

    def Program(self):
        secim = self.Menu()

        if secim == 1:
            self.bakiye()
        if secim == 2:
            self.kkborc()
        if secim == 3:
            self.paracek()
        if secim == 4:
            self.parayatir()
        if secim == 5:
            self.cikis()

    def Menu(self):
        secim=int(input("""Merhabalar {}'a Hoşgeldiniz Sayın {} {}.\n\nLütfen Yapmak istediğinz işlemş seçinzi... \n\n[1] Bakiye sorgulama\n[2] Kredi kartı Borç Sorgulama\n[3] Para çekme\n[4] Para Yatırma\n[5] KArt iade\n\nSeçim:""".format(self.atmad,TakilanKart.ad,TakilanKart.soyad)))
        if 1>secim or secim>5:
            print("\n\nLütfen 1 ve 5 arasıdan geçerli Bir Değer giriniz...\nAna menüye Dönülüyor...")
            self.Program()
        else:
            return secim

    def bakiye(self):
        print("kart bakiyesi: {}".format(TakilanKart.hesapbakiye))
        self.dongu=False
        self.menuDon()

    def kkborc(self):
        print("Kredi kartı  Borcunuz {} son Ödeme tarihli {} TL'dir.".format(TakilanKart.sonodeme,TakilanKart.kredikartborc))
        self.dongu=False
        self.menuDon()

    def paracek(self):
        miktar=int(input("Lütfen çekeceğiniz Tutarı Giriniz:..."))
        YeniMiktar=TakilanKart.hesapbakiye-miktar
        if TakilanKart.hesapbakiye<miktar:
            print("Yetersiz Bakiye")
            self.menuDon()
        else:
            print("Lütfen Paranızı sayarak Alınız .Hesabınızda kalan Tutar {} TL'dir".format(YeniMiktar))
            self.menuDon()

    def parayatir(self):
        miktar2=int(input("lütfen yatıracağınız tutuarı giriniz:"))
        YeniMiktar2=TakilanKart.hesapbakiye+miktar2
        print("para yatırma işlemi Başarıyla Gerçekleştirilmiltir.Hesabınızın Yeni Bakiyesi {} TL'dir".format(YeniMiktar2))
        self.menuDon()

    def cikis(self):
        print("Bankamızı Tercih Ettiğiniz iin teşekür ederiz,iyi günler dileriz...")
        self.dongu=False
        exit()

    def menuDon(self):
        x=int(input("""Ana menüye dönmek için Lütfen 7 tuşuna basınız.Kart iade içim 5'e basınız: """))
        if x==7:
            self.Program()
        elif x==5:
            self.cikis()

Banka = ATM("xBank")
while Banka.dongu:
    Banka.Program()
