#!/usr/bin/env python
# coding: utf-8

# In[53]:


def sifreKontrol():
    flag=True 
    sayac=3
    sifre="1234"
    while flag:
        gsifre=input("lütfen şifrenizi giriniz")
        if gsifre==sifre:
            print("şifreniz doğru giriş yapılıyor")
            return True
            flag=False
            break
        elif gsifre!=sifre:
            print("şifreniz yanlış tekrar deneyiniz deneme hakkınız {}".format(sayac))
            sayac=sayac-1
        if sayac==-1:
            print("deneme hakkınız bitmiştir şifreniz yanlış")
            return False
            flag=False
def paraCek(bakiye,deger):
    if bakiye>deger:
        bakiye=bakiye-deger
        return bakiye
    elif bakiye<deger:
        print("çekmek istediğiniz değer bakiyenizden fazladır")
        return bakiye
def paraYatır(bakiye,ydeger):
    bakiye=bakiye+ydeger
    return bakiye
def borcOdeN(borc,miktar):
    if miktar<borc:
        borc=borc-miktar
        return borc
    elif miktar==borc:
        borc=0
        return borc 
    elif miktar>borc:
        borc=0
        pustu=miktar-borc
        print("para üstünüz = {}".format(pustu))
        return borc
def borcOdeB(bakiye,borc):
    if borc>bakiye:
        print("borcunuz bakiyeden yüksek")
        borc=borc-bakiye
        bakiye=0
        return borc,bakiye
    elif bakiye>=borc:
        bakiye=bakiye-borc
        borc=0
        return bakiye,borc
import random


            
menu="""-------------------------------------
        1-Bakiye Sorgulama 2-Para Çekme
        3-Para Yatırma     4-Borç Sorgulama
        5-Borç Ödeme       6-USD al
        7-Çıkış
        -------------------------------------"""

if sifreKontrol()==True:
    flag=True
    bakiye=1000
    borc=500
    while flag:
        
        print(menu)
        secim=input("lütfen yapmak istediğiniz işelmi seçiniz")
        if secim=="1":
            print("bakiyeniz {}TL".format(bakiye))
        elif secim=="2":
            deger=int(input("çekmek istediğiniz değeri giriniz"))
            bakiye=paraCek(bakiye,deger)
            print("güncel bakiyeniz {}".format(bakiye))
        elif secim=="7":
            print("çıkış yapılıyor...")
            flag=False
        elif secim=="3":
            ydeger=int(input("lütfen yatırmak istediğiniz değeri giriniz"))
            bakiye=paraYatır(bakiye,ydeger)
            print("güncel bakiyeniz {}".format(bakiye))
        elif secim=="4":
            print("güncel borcunuz {}".format(borc))
        elif secim=="5":
            print("""------------------
                     1-nakit ödeme
                     2-bakiyeden ödeme
                     ------------------""")
            secim2=input("lütfen seçiminizi giriniz")
            if secim2=="1":
                miktar=int(input("lütfen yatırmak istediğiniz miktarı giriniz"))
                borc=borcOdeN(borc,miktar)
                print("şuanki borcunuz{}".format(borc))
            elif secim2=="2":
                bakiye,borc=borcOdeB(bakiye,borc)
                print("şuanki borcunuz {}TL ve şuanki bakiyeniz {}TL".format(borc,bakiye))
            else:
                print("yanlış bir giriş yaptınız")
        elif secim=="6":
            bakiye=random.random()
            print(":/ :0 bakiyeniz {} USD :0 :/".format(bakiye))
        else:
            print("hatalı giriş yaptınız lütfen tekrar deneyiniz...")
                
            
                
        
                
            
            
        
            
            


# In[31]:


def borcOdeB(bakiye,borc):
    if borc>bakiye:
        print("borcunuz bakiyeden yüksek")
        borc=borc-bakiye
        bakiye=0
        return borc,bakiye
    elif bakiye>=borc:
        borc=0
        
        return bakiye-borc,borc
    
borcOdeB(100,50)


# In[43]:


import random


# In[ ]:




