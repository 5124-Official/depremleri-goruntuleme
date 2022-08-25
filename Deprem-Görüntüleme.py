import json
from os import system
from time import sleep
import requests                                 #5124
from colorama import init, Fore
init(autoreset=True)

while True:

    print(Fore.RED+"            5 1 2 4 - O f f i c a l \n")
    print(Fore.RED+"Tür         "+Fore.CYAN+"Tarih & Saat           "+Fore.GREEN+"Yer           "+Fore.RED+"Büyüklük        "+Fore.YELLOW+"Derinlik")
    print("-------------------------------------------------------------------------------")

    json = requests.post("https://api.orhanaydogdu.com.tr/deprem/live.php").json() #Deprem verilerini api ile json türünden çekiyoruz
    
    for item in json["result"]: # Json verilerini ayıklıyoruz 
        tarih = item["date"]
        yer = item["lokasyon"]
        büyüklük = item["mag"]
        derinlik = item["depth"]

        print(Fore.RED+"Deprem ! "+Fore.CYAN+tarih+Fore.GREEN+" "+yer+Fore.RED+" "+str(büyüklük)+Fore.YELLOW+" "+str(derinlik)) #Depremleri yazdırıyoruz

    sleep(13)
    system("cls")#Terminali temizleme komutu Not: Sadece windows
    sleep(0.6)