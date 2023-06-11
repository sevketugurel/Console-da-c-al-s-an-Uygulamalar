import re
import time

class Kayıt:
    def __init__(self,programAd):
        self.programAd=programAd
        self.dongu=True

    def program(self):
        secim=self.menu()

        if secim=="1":
            print("Kayıt Ekleme Menüsüne yönlendiriliyorsunuz...")
            time.sleep(1)
            self.kayıtEkle()

        if secim=="2":
            print("Kayıt silme Menüsüne yönlendiriliyorsunuz...")
            time.sleep(3)
            self.kayıtCıkar()
        
        if secim=="3":
            print("Verilere Erişiliyor")
            time.sleep(3)
            self.kayıtOku()

        if secim=="4":
            self.cikis()


    def menu(self):
        def Kontrol(secim):
            if re.search("[^1-4]",secim):
                raise Exception("Lütfen 1 ve 4 arasında geçerli bir seçim yapınız...")
            elif len(secim)!=1:
                raise Exception("Lütfen 1 ve 4 arasında geçerli bir seçim yapınız...")
            
        while True:
            try:
                secim=input("Merhabalar, {} otomsayon Sistemine Hoşgeldiniz.\n\nLütfen Yapmak istediğiniz işlemi seçiniz...\n\n[1]-Kayıt Ekle\n[2]-Kayıt sil\n[3]-Kayıt oku\n[4]-Çıkış\n\n".format(self.programAd))
                Kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(1)
            else:
                break
        return secim
 
    def kayıtEkle(self):
        def kontrolAd(Ad):
            if Ad.isalpha()==False:
                raise Exception("Adınız sadece alfabeetik karakterlerden oluşmalıdır...")
        while True:
            try:
                Ad=input("Adınız: ")
                kontrolAd(Ad)
            except Exception as hataAd:
                print(hataAd)
                time.sleep(1)
            else:
                break
                    
                
        def kontrolSoyad(Soyad):
            if Soyad.isalpha()==False:
                raise Exception("Soyadınız sadece alfabeetik karakterlerden oluşmalıdır...")
        while True:
            try:
                Soyad=input("Soyadınız: ")
                kontrolAd(Soyad)
            except Exception as hataSoyad:
                print(hataSoyad)
                time.sleep(1)
            else:
                break

        def kontrolYas(yas):
            if yas.isdigit()==False:
                raise Exception("Yaşınız sadece rakamlardan oluşmalıdır...")
        while True:
            try:
                yas=input("Yaşınız: ")
                kontrolYas(yas)
            except Exception as hataYas:
                print(hataYas)
                time.sleep(1)
            else:
                break

        def kontrolTC(TC):
            if TC.isdigit()==False:
                raise Exception("Kimlik Numaranız sadece rakamlardan oluşmalıdır...")
            elif len(TC)!=11:
                raise Exception("Kimlik numaranız 11 Karakterden oluşmalıdır...")

        while True:
            try:
                TC=input("Kimlik Numaranız: ")
                kontrolTC(TC)
            except Exception as hataTC:
                print(hataTC)
                time.sleep(1)
            else:
                break
                
        def kontrolmail(mail):
            if not re.search("@" and ".com",mail):
                raise Exception("\nGeçerli bir mail Adresi giriniz...")
            
        while True:
            try:
                mail=input("mailiniz: ")
                kontrolmail(mail)
            except Exception as hatamail:
                print(hatamail)
                time.sleep(1)
            else:
                break
        with open("/Users/sevketugurel/Desktop/Bilgiler.txt","r",encoding="utf-8") as Dosya:
            satırSayısı=Dosya.readlines()
        if len(satırSayısı)==0:#yani dosya boş mu diye bakıyoruz çünkü id atayacağız
            id=1
        else:
            with open("/Users/sevketugurel/Desktop/Bilgiler.txt","r",encoding="utf-8") as Dosya:
                id=int(Dosya.readlines()[-1].split("-")[0])+1
            
            #Burada dosyanın satır numarasını buluyoruz o da satırın son elemanını bul o elemanı 
            #"-" ile böl ve ilk elemanını al oluyor örneğin ["3-c"] bunu "-"ile bölelim ["3","c"]
            #ilk elemanını alalım "3" +1 yapıp sonraki satır sayısını buluyoruz.
        
        with open("/Users/sevketugurel/Desktop/Bilgiler.txt","a+",encoding="utf-8") as Dosya:
            Dosya.write("{0}-{1} {2} {3} {4} {5}\n".format(id,Ad,Soyad,yas,TC,mail))
            print("\nVeriler işlenmiştir...")
        self.menuDon()

    def kayıtCıkar(self):
        y=input("\nLütfen silmek istediğiniz kişinin Id Numarasını Giriniz...:")
        with open("/Users/sevketugurel/Desktop/Bilgiler.txt","r",encoding="utf-8") as Dosya:
            liste=[]
            liste2=Dosya.readlines()
            for i in range(0,len(liste2)):
                liste.append(liste2[i].split("-")[0])

        del liste2[liste.index(y)]

        with open("/Users/sevketugurel/Desktop/Bilgiler.txt","w+",encoding="utf-8") as yeniDosya:
            for i in liste2:
                yeniDosya.write(i)
        print("\nKayıt siliniyor...")
        time.sleep(1)
        print("\nKayıt Başarıyla Silinmiştir...")
        self.menuDon()

    def kayıtOku(self):
        with open("/Users/sevketugurel/Desktop/Bilgiler.txt","r",encoding="utf-8") as Dosya:
            for i in Dosya:
                print(i)
            self.menuDon()

    def cikis(self):
        print("Otomasyondan Çıkılıyor. Teşekkürler")
        self.dongu=False
        exit()

    def menuDon(self):
        while True:
            x=input("\nAna menüye Dönmek için 6'ya,çıkmak için Lütfen 5'e basınız...")
            if x=="6":
                print("Ana menüye dönülüyor...")
                time.sleep(1)
                self.program()
                break
            elif x=="5":
                self.cikis()
                break
            else:
                print("\nLütfen geçerli bir seçim yapınız...")

Sistem=Kayıt("Anlaşılır Ekonomi")
while Sistem.dongu:
    Sistem.program()








 