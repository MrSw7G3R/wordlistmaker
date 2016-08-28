#-*- coding: cp857 -*-
import time,os,sys,random,re,traceback
os.system("title Dr.UK Wordlist Olusturucu")
reload(sys)
sys.setdefaultencoding('cp857')
DrUK = True
from itertools import permutations
wordlist = []
values = []
bilgiler = {}
renkler = ['\033[95m','\033[94m','\033[93m','\033[91m','\033[1m']
def retsekil(metin="Bos gecildi"):
    return random.choice(renkler) + "["+time.strftime("%H:%M:%S")+ "]" + metin.decode('utf-8').encode(sys.stdout.encoding) + '\033[0m'
def sekilyaz(metin):
    print random.choice(renkler) + "["+time.strftime("%H:%M:%S")+ "]" + metin.decode('utf-8').encode(sys.stdout.encoding) + '\033[0m'
def ekle(ad,bilgi):
    if bilgi == "":
        sekilyaz("Boş girildi.")
    else:
        if len(bilgi.split(" ")) > 1:
            tmp = len(bilgi.split(" "))
            for sayi in range(0,tmp):
                bilgiler[ad + str(sayi)] = bilgi.split(" ")[sayi]
        else:
            bilgiler[ad.strip()] = bilgi



info = """
-------------------------------------------------------------------
Dr.UK Wordlist Oluşturucu
Çıkan sorulara cevap ver.
Başka eklemek istediğin şey syntax'ı
Eklenecekad:Bilgi

Türkçe karakterler programda sorun çıkartır.
Zaten Facebook gibi yerlerde türkçe karakter kullanılmaz.
-------------------------------------------------------------------
"""
def premadewordlist():
    sekilyaz("Genelde kullanılan şifreler yazılıyor...")
    donald = bilgiler["ad"]
    wordlist.append("abcd1234")
    wordlist.append("password")
    wordlist.append("password123")
    wordlist.append("123password")
    wordlist.append("1234abcd")
    wordlist.append("abcd1234")
    wordlist.append("q1w2e3r4")
    wordlist.append("696969")
    wordlist.append("123456")
    wordlist.append("password")
    wordlist.append("sifre123")
    wordlist.append("1234567890")
    wordlist.append("letmein")
    wordlist.append("shadow")
    wordlist.append("trustno1")
    wordlist.append("fuckyou123")
    wordlist.append(donald + "123")
    wordlist.append(donald + "1234")
    wordlist.append(donald + "12345")
    wordlist.append(donald + "123456")
    wordlist.append(donald + "1234567")
    wordlist.append(donald + "12345678")
    wordlist.append(donald + bilgiler["yil"])
    wordlist.append(donald + "31")
    wordlist.append(donald + "fb1907")
    wordlist.append(donald + "fener1907")
    wordlist.append(donald + "fenerbahce1907")
    wordlist.append(donald + "gs1905")
    wordlist.append(donald + "galatasaray1905")
    wordlist.append(donald + "bjk1903")
    wordlist.append(donald + "besiktas1903")
    wordlist.append(donald + "741852963")
    wordlist.append(donald + "000")
    wordlist.append("xxx" + donald + "xxx")
    wordlist.append(donald + "741852963")
    reverseadd(donald , "123")
    reverseadd(donald , "1234")
    reverseadd(donald , "12345")
    reverseadd(donald , "123456")
    reverseadd(donald , "1234567")
    reverseadd(donald , "12345678")
    reverseadd(donald , bilgiler["yil"])
    reverseadd(donald , "31")
    reverseadd(donald , "fb1907")
    reverseadd(donald , "fener1907")
    reverseadd(donald , "fenerbahce1907")
    reverseadd(donald , "gs1905")
    reverseadd(donald , "galatasaray1905")
    reverseadd(donald , "bjk1903")
    reverseadd(donald , "besiktas1903")
    reverseadd(donald , "741852963")
    reverseadd(donald , "000")
    reverseadd(donald , "741852963")
    wordlist.append(donald + bilgiler["telno"][7:11])
    wordlist.append(donald + bilgiler["telno"][5:11])
    wordlist.append(donald + bilgiler["telno"][:4])
    wordlist.append(donald + bilgiler["telno"][:])
    reverseadd(donald , bilgiler["telno"][7:11])
    reverseadd(donald , bilgiler["telno"][5:11])
    reverseadd(donald , bilgiler["telno"][:4])
    reverseadd(donald , bilgiler["telno"][:])

def reverseadd(item1,item2):
    wordlist.append(item2+item1)



def karistir():
    sekilyaz("Kişiye özel şifreler yazılıyor...")
    values = list(bilgiler.values())
    for sayi in range(1,len(values) + 1):
        if sayi > 3:
            break
        sekilyaz("Şu anda %s kelimelik permutasyon yapılıyor..." % sayi)
        for tuples in permutations(values,sayi):
            za = ''.join(tuples)
            wordlist.append(za)
            #sekilyaz(za)










def main():
    sekilyaz(info)
    ad = raw_input(retsekil("Adı: "))
    ekle("ad",ad)
    ad2 = raw_input(retsekil("2. Adı: "))
    ekle("ad2",ad2)
    soyad = raw_input(retsekil("Soyadı: "))
    ekle("soyad",soyad)
    dogum = raw_input(retsekil("Dogum gunu: ")).split('.')
    ekle("gun",dogum[0])
    ekle("ay",dogum[1])
    ekle("yil",dogum[2])
    annead = raw_input(retsekil("Annesinin adi: "))
    ekle("annead",annead)
    babaad = raw_input(retsekil("Babasinin adi: "))
    ekle("babaad",babaad)
    hayvan = raw_input(retsekil("Hayvaninin adi: "))
    ekle("hayvan",hayvan)
    futboltakimi = raw_input(retsekil("Sevdiği futbol takımı: "))
    ekle("futboltakimi",futboltakimi)
    baskettakimi = raw_input(retsekil("Sevdiği basketbol takımı: "))
    ekle("baskettakimi",baskettakimi)
    sarkici = raw_input(retsekil("Sevdiği şarkıcı: "))
    ekle("sarkici",sarkici)
    oyuncu = raw_input(retsekil("Sevdiği oyuncu: "))
    ekle("oyuncu",oyuncu)
    basketci= raw_input(retsekil("Sevdiği basketbol oyuncusu: "))
    ekle("basketoyuncu",basketci)
    yemek = raw_input(retsekil("Sevdiği yemek: "))
    ekle("yemek",yemek)
    hayvanturu = raw_input(retsekil("En sevdiği hayvan türü: "))
    ekle("hayvanturu",hayvanturu)
    kari = raw_input(retsekil("Karısının adı: "))
    ekle("kariad",kari)
    cocukad = raw_input(retsekil("Çocuğunun adı: "))
    ekle("cocukad",cocukad)
    telno = raw_input(retsekil("Telefon numarası: "))
    ekle("telno",telno)
    while DrUK:
        sekilyaz("Başka eklemek istediğin bir şey varsa yaz. Bitirmek için X yaz.")
        baska = raw_input("["+time.strftime("%H:%M:%S")+ "]")
        if baska.lower() == "x":
            break
        try:
            ekle(baska.split(":")[0],baska.split(":")[1])
            sekilyaz("Eklenen, %s'ye %s" % (baska.split()[0],baska.split()[1]))
        except:
            continue

    with open("bilgiler.txt","a") as f:
        sekilyaz("Bilgiler bir sonraki kullanım için saklanıyor...")
        f.writelines("-"*50)
        f.writelines("\n")
        for key,value in bilgiler.items():
            f.writelines("%s:%s" % (key,value))
            f.writelines("\n")
        f.writelines("-"*50)
        f.writelines("\n")
    sekilyaz("Wordlist oluşturulmaya başlanıyor...")
    premadewordlist()
    karistir()
    with open("%swordlist.txt" % bilgiler["ad"],"a") as f:
        f.writelines("-"*50)
        f.writelines("\n")
        for i in wordlist:
            f.writelines(i)
            f.writelines("\n")
        f.writelines("-"*50)
        f.writelines("\n")








if __name__ == '__main__':
    try:
        main()
    except Exception,e:
        print "\n"
        print traceback.print_exc()
        print bilgiler
