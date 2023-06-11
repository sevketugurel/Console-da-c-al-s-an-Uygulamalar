import json
import re
import random
import time

class Site:
    def __init__(self):
        self.dongu=True
        self.veriler=self.veriAl()


    def program(self):
        secim=self.menu()

        if secim=="1":
            self.giris()
        if secim=="2":
            self.kayıtol()
        if secim=="3":
            self.cikis()
            
    def menu(self):
        def kontrol(secim):
            if re.search("[^1-3]",secim):
                raise Exception("Lütfen 1-3 Arasında bir seçim yapınız!!")
            elif len(secim)!=1:
                raise Exception("Lütfen 1-3 Arasında bir seçim yapınız!!")
        while True:
            try:
                secim=input("\n\nMerhabalar,Şevket Uğurel Sitesine hoşgeldiniz\n\nLütfen Yapmak İstediğiniz İşlemi Seçiniz\n\n[1]-Giriş\n[2]-Kayıt Ol\n[3]-Çıkış\n\n")
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(1)
            else:
                break
        return secim
    def giris(self):
        print("Giriş menüsüne yönlendiriliyorsunuz...")
        time.sleep(1)   
        kullanıcıAdı=input("Lütfen Kullanıcı Adı giriniz...")
        Sifre=input("lütfen Şifrenizi Giriniz...")

        sonuc=self.girisKontrol(kullanıcıAdı,Sifre)
        if sonuc==True:
            self.girisBasarili()
        else:
            self.girisBasarisiz()

    def girisKontrol(self,kullanıcıAdı,Sifre):
        self.veriler=self.veriAl()
        try:
            for kullanıcı in self.veriler["Kullanıcılar"]:
                if kullanıcı["Kullanıcıadı"]==kullanıcıAdı and kullanıcı["Sifre"]==Sifre:
                    return True
        except KeyError:
            return False
        return False
            

    def girisBasarili(self):
        print("Kontrol Ediliyor...")
        time.sleep(1)
        print("Giriş başarılı. Şevket Uğurel sitesine hoşgeldiniz...")
        self.sonuc=False
        self.dongu=False


    def girisBasarisiz(self):
        print("Kullanıcı Adı Veya şifre hatalı!!")
        time.sleep(1)
        self.menuDon()
        
    def kayıtol(self):
        def kontrolKa(kullanıcıAdı):
            if len(kullanıcıAdı)<8:
                raise Exception("Kullanıcı adınız en az 8 karakterden oluşmalıdır!!")
        while True:
            try:
                kullanıcıAdı=input("Kullanıcı Adınız: ")
                kontrolKa(kullanıcıAdı)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break

        def kontrolsifre(Sifre):
            if len(Sifre)<8:
                raise Exception("Şifreniz en az 8 karakterden oluşmalıdır!!")
            elif  not re.search("[1-9]",Sifre):
                raise Exception("Şifrenizde en az bir rakam olamlıdır!!")
            elif   not re.search("[A-Z]",Sifre):
                raise Exception("Şifrenizde en az bir büyük harf olmalıdır!!")
            elif   not re.search("[a-z]",Sifre):
                raise Exception("Şifrenizde en az bir küçük harf olmalıdır!!")

        while True:
            try:
                Sifre=input("Şifreniz: ")
                kontrolKa(Sifre)
            except Exception as hatasi:
                print(hatasi)
                time.sleep(1)
            else:
                break

        def kontrolKa(Mail):
            if not re.search(".com" and "@",Mail):
                raise Exception("Geçerli bir mail Adresi Giriniz!!")
        while True:
            try:
                Mail=input("Mail Adresiniz: ")
                kontrolKa(Mail)
            except Exception as hatamail:
                print(hatamail)
                time.sleep(1)
            else:
                break
        kayıtsonuc=self.kayıtVarMı(kullanıcıAdı,Mail)
        if kayıtsonuc==True:
            print("Bu kullanıcı Adı ve Mail sistemde Zaten kayıtlı!!")
        else:
            aktivasyonKodu=self.aktivasyonGonder()
            durum=self.aktivasyonKontrol(aktivasyonKodu)
        while True:
            if durum==True:
                self.veriKaydet(kullanıcıAdı,Sifre,Mail)
                break
            else:
                print("Aktivasyon kodunuz hatalı...")
                time.sleep(1)
                self.menuDon()
    def kayıtVarMı(self,kullanıcıAdı,Mail):
        self.veriler=self.veriAl()
        try:
            for kullanıcı in self.veriler["Kullanıcılar"]:
                if kullanıcı["KullanıcıAdı"]==kullanıcıAdı and kullanıcı["Mail"]==Mail:
                    return True
        except KeyError:
            return False
        return False

    def aktivasyonGonder(self):
        with open("/Users/sevketugurel/Desktop/Aktivasyon.txt","w",encoding="utf-8") as Dosya:
            aktivasyon=str(random.randint(10000,99999))
            Dosya.write("Aktivasyon Kodunuz: "+aktivasyon)
            return aktivasyon

    def aktivasyonKontrol(self,aktivasyonKodu):
        alınanAktivasyon=input("LÜtfen mailinize gelen aktivasyon kodunu giriniz: ")
        if aktivasyonKodu==alınanAktivasyon:
            return True
        else:
            return False

    def veriAl(self):
        try:
            with open("/Users/sevketugurel/Desktop/Kullanıcılar.json","r",encoding="utf-8") as Dosya:
                veriler=json.load(Dosya)
        except FileNotFoundError:
            with open("/Users/sevketugurel/Desktop/Kullanıcılar.json","w",encoding="utf-8") as Dosya:
                Dosya.write("{}")
            with open("/Users/sevketugurel/Desktop/Kullanıcılar.json","r",encoding="utf-8") as Dosya:
                veriler=json.load(Dosya)
        return veriler
        
    def veriKaydet(self,kullanıcıAdı,Sifre,Mail ):
        self.veriler=self.veriAl

        try:
            self.veriler["Kullanıcılar"].append({"Kullanıcıadı":kullanıcıAdı,"Sifre":Sifre,"Mail":Mail})
        except TypeError:
            self.veriler["Kullanıcılar"]=list()
            self.veriler["Kullanıcılar"].append({"Kullanıcıadı":kullanıcıAdı,"Sifre":Sifre,"Mail":Mail})

        with open("/Users/sevketugurel/Desktop/Kullanıcılar.txt","w",encoding="utf-8") as Dosya:
            json.dump(self.veriler,Dosya,ensure_ascii=False,indent=4)
            print("Kayıt başaralı şekilde oluşturullmuştur...")
        self.menuDon()

    def cikis(self):
        print("siteden çıkılıyor...")
        time.sleep(1)
        self.dongu=False
        exit()
    
    def menuDon(self):
        x=input("Ana menüye Dönmek için 5'e ,Çıkmak için Lütfen 4'e basınız...: ")
        if x=="5":
            print("Ana menüye Dönülüyor...")
            time.sleep(1)
            self.program()             
        elif x=="4":
            self.cikis()
        else:
            print("Lütfen Geçerli Bir seçim Yapınız!!")

Sistem=Site()

while Sistem.dongu:
    Sistem.program()
    


    






