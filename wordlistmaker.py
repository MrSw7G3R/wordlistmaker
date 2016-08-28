#-*- coding: cp857 -*-
import time,os,sys,random,re,traceback
os.system("title MrSw7g3r Wordlist Maker")
reload(sys)
sys.setdefaultencoding('cp857')
MrSw7g3r = True
from itertools import permutations
wordlist = []
values = []
bilgiler = {}
renkler = ['\033[95m','\033[94m','\033[93m','\033[91m','\033[1m']
def retsekil(metin="Empty"):
    return random.choice(renkler) + "["+time.strftime("%H:%M:%S")+ "]" + metin.decode('utf-8').encode(sys.stdout.encoding) + '\033[0m'
def sekilyaz(metin):
    print random.choice(renkler) + "["+time.strftime("%H:%M:%S")+ "]" + metin.decode('utf-8').encode(sys.stdout.encoding) + '\033[0m'
def ekle(ad,bilgi):
    if bilgi == "":
        sekilyaz("Empty.")
    else:
        if len(bilgi.split(" ")) > 1:
            tmp = len(bilgi.split(" "))
            for number in range(0,tmp):
                bilgiler[ad + str(number)] = bilgi.split(" ")[number]
        else:
            bilgiler[ad.strip()] = bilgi



info = """
-------------------------------------------------------------------
MrSw7g3r Wordlist Maker
Github: https://github.com/MrSw7G3R


Inspired from Elliot,
This tool takes all the information from user
and uses permutations to spread all the words so
you don't miss any passwords.


If you want to add another word you can use the last part.
The syntax for last part is
Nameofinformation:information

Lastly, I'm not native speaker. So forgive me
for my bad english :p
-------------------------------------------------------------------
"""
def premadewordlist():
    sekilyaz("Writing common passwords")
    donald = bilgiler["name"]
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
    wordlist.append(donald + bilgiler["year"])
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
    reverseadd(donald , bilgiler["year"])
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



def mix():
    sekilyaz("Writing the permutations...")
    values = list(bilgiler.values())
    for number in range(1,len(values) + 1):
        if number > 3:
            break
        sekilyaz("Now making %s words permutation." % number)
        for tuples in permutations(values,number):
            za = ''.join(tuples)
            wordlist.append(za)
            #sekilyaz(za)


def main():
    sekilyaz(info)
    name = raw_input(retsekil("Name: "))
    ekle("name",name)
    secname = raw_input(retsekil("Second Name: "))
    ekle("secname",secname)
    lastname = raw_input(retsekil("Soyadı: "))
    ekle("lastname",lastname)
    dogum = raw_input(retsekil("Birthday(xx.x.xxxx): ")).split('.')
    ekle("day",dogum[0])
    ekle("month",dogum[1])
    ekle("year",dogum[2])
    momname = raw_input(retsekil("Mom's name: "))
    ekle("momname",momname)
    fathername = raw_input(retsekil("Father's name: "))
    ekle("fathername",fathername)
    animalname = raw_input(retsekil("Animal's name: "))
    ekle("animalname",animalname)
    soccerteam = raw_input(retsekil("Soccer Team: "))
    ekle("soccerteam",soccerteam)
    basketteam = raw_input(retsekil("Basketball Team: "))
    ekle("basketteam",basketteam)
    singer = raw_input(retsekil("Favorite Singer: "))
    ekle("singer",singer)
    oyuncu = raw_input(retsekil("Favorite Holywood Famous: "))
    ekle("famous",oyuncu)
    basketci= raw_input(retsekil("Favorite Basketball Player: "))
    ekle("basketplayer",basketci)
    food = raw_input(retsekil("Favorite Food: "))
    ekle("food",food)
    hayvanturu = raw_input(retsekil("Favorite animal type: "))
    ekle("animaltype",hayvanturu)
    kari = raw_input(retsekil("Wife Name: "))
    ekle("wifename",kari)
    cocukad = raw_input(retsekil("Child's name: "))
    ekle("childname",cocukad)
    telno = raw_input(retsekil("Tel no: "))
    ekle("telno",telno)
    while MrSw7g3r:
        sekilyaz("If you want to add something different, use me! Else, type x.")
        baska = raw_input("["+time.strftime("%H:%M:%S")+ "]")
        if baska.lower() == "x":
            break
        try:
            ekle(baska.split(":")[0],baska.split(":")[1])
            sekilyaz("Added, %s to %s" % (baska.split()[0],baska.split()[1]))
        except:
            continue

    with open("information.txt","a") as f:
        sekilyaz("Saving information for future uses...")
        f.writelines("-"*50)
        f.writelines("\n")
        for key,value in bilgiler.items():
            f.writelines("%s:%s" % (key,value))
            f.writelines("\n")
        f.writelines("-"*50)
        f.writelines("\n")
    sekilyaz("Wordlist maker started...")
    premadewordlist()
    mix()
    with open("%swordlist.txt" % bilgiler["name"],"a") as f:
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
