import time
import random
class Kumanda :
    def __init__(self,tv_durum = "kapalı",tv_ses = 0 , kanal_listesi = ["Trt"],kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tv_Aç(self):
        print("televizyon" , self.tv_durum)
        if self.tv_durum == "açık" :
            print("tv zaten açık")
        else :
            print("televizyon açılıyor..")
            self.tv_durum = "açık"
    def tv_Kapa (self) :
        print("televizyon" , self.tv_durum)
        if self.tv_durum == "kapalı" :
            print("tv zaten kapalı")
        else :
            print("televizyon kapatılıyor..")
            self.tv_durum = "kapalı"
    def ses(self) :
        while True :
            print("ses açmak için '>' , ses kısmak için '<' çıkmak için 'E' basınız.")
            self.seskomutu = input("işlem giriniz : ")
            if self.seskomutu == ">" :
                if self.tv_ses == 31  :
                    print("en yüksek ses " )
                    continue
                self.tv_ses += 1
                print(self.tv_ses)
            elif self.seskomutu == "<" :
                if self.tv_ses == 0 :
                    print("ses : 0 ")
                    continue
                self.tv_ses -= 1
                print(self.tv_ses)
            elif self.seskomutu == "e" :
                break
            else :
                print("gecersiz işlem")
    def kanal_ekleme (self) :
        self.kanallar = input("eklemek istediğiniz kanalı seciniz : ")
        self.kanallar = self.kanallar.split()
        for x in self.kanallar :
            self.kanal_listesi.append(x),
            print(x , "ekleniyor.")
            time.sleep(1)
            print(x , "eklendi.")
    def kanaldegistirme (self):
        print("bir üst kanal için : 8 , bir alt kanal için 2 tuşlayınız.")
        self.kanaldegis = input(" : ")
        if self.kanaldegis == "8" :
            self.kanal = self.kanal_listesi[self.kanalindexi()+1]
            print(self.kanal)
        elif self.kanaldegis == "2" :
            self.kanal = self.kanal_listesi[self.kanalindexi() + -1]
            print(self.kanal)
        else :
            print("Geçersiz işlem ")

    def kanalindexi (self)  :
        return self.kanal_listesi.index(self.kanal)
    def rastgelekanal (self) :
        rastgale = random.randint(0,len(self.kanal_listesi )-1)
        self.kanal = self.kanal_listesi[rastgale]
        print(self.kanal)
    def bilgilerigöster  (self) :
        print(f"Tv Durumu : {self.tv_durum}\nTv Ses : {self.tv_ses}\nTv Kanal listesi : {self.kanal_listesi}\nSecili kanal : {self.kanal}")
kumandamız = Kumanda()
print("Televizyon komutları".center(100, "*"),
      "\n1- Televizyonu Aç\n2- Televizyonu kapa\n3-Kanal değiştir\n4-Ses\n5-Kanalı öğren\n6-Rastgale Kanal\n7-Kanal ekle\n8-kanal listesi)")
kumandamız.bilgilerigöster()
while True :


    komut = int(input("Komutunuz : "))
    if komut == 1 :
       kumandamız.tv_Aç()
    elif komut == 2 :
        kumandamız.tv_Kapa()
        break
    elif komut == 3 :
        kumandamız.kanaldegistirme()
    elif komut == 4 :
        kumandamız.ses()
    elif komut == 5 :
       print( kumandamız.kanal)
    elif komut == 6 :
        kumandamız.rastgelekanal()
    elif komut == 7 :
        kumandamız.kanal_ekleme()
    elif komut == 8 :
        print(kumandamız.kanal_listesi)
    else :
        print("gecersiz işlem")