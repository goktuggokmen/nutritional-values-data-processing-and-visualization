# -*- coding: utf-8 -*-
"""BESİN DEĞERLERİ VERİLERİNİN İŞLENMESİ VE GÖRSELLEŞTİRİLMESİ.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YYGFAknRHtbj98ZRKMMYtkFJ62dBd5Gi

## ***PROJEMİZİN AMACI GIDALARIN BESİN DEĞERLERİNİ İŞLEYEREK VERİLERİ GÖRSELLEŞTİRMEKTİR.***

# 1.HAZIRLAYANLAR
# *   Göktuğ GÖKMEN
# *   Muhammet Fatih ACUN
# *   Metehan ÇALLI 
# *   Zehra ASLAN
Kaynak ---> Hacettepe Üniversitesi Sağlık Bilimleri Fakültesi Beslenme Ve Diyetetik Bölümü

# 2.KULLANILACAK KÜTÜPHANELERİN YÜKLENMESİ
"""

import matplotlib.pyplot as plt #numpy çizim kütüphanesi 
import seaborn as sns #istatiksel grafikleri çizdirmek için gerekli kütüphane
import pandas as pd #veri analiz ve işleme için kullanılan kütüphane 
import numpy as np #büyük, çok boyutlu diziler ve matrisler için destek eklerken, bu dizilerde çalışmak için yüksek düzeyli matematiksel işlevlerin geniş bir koleksiyonudur.
import csv #Virgülle ayrılmış değerler dosyası, değerleri ayırmak için virgül kullanan sınırlandırılmış bir metin dosyasıdır. Dosyanın her satırı bir veri kaydıdır. Her kayıt virgülle ayrılmış bir veya daha fazla alandan oluşur. Alan ayırıcı olarak virgül kullanılması, bu dosya formatı için adın kaynağıdır.

"""# 3.DOSYALARI OKUMA """

yas_enerji = pd.read_excel("yas_enerji.xlsx") #yaş-enerji ilişkisi içeren tablonun okunması

data =pd.read_excel("pyhton_proje.xlsx") #besin değerlerini içeren tablonun okunması

"""#4.ÖNCELİKLE VERİLERİMİZE BİR GÖZ ATALIM"""

#veriye dair genel bilgiler
data.info()

# ilk 30 veri #

data.head(30)

# son 30 veri#
data.tail(30)

data.describe() #kolonların istatiksel bilgileri

data.columns #kolonların adlarını verir

# veri dosyasının boyutunu inceleyelim #

data.ndim

#veri boyutu
data.shape

#Kullanıcı tarafından girilen bir besinin besin değerlerine erişme 
copy_data = data.set_index('BESINLER') #data'nın içeriğini "BESINLER" sütununu index olacak şekilde copy_data'ya kopyalıyoruz
besin = input("Besin degerlerini merak ettiğiniz yiyecek/icecek : ") #besin değerleri merak edilen besini girdi olarak kullanıcıdan alma
new_data = copy_data.loc[besin] #"BESINLER" sütununu indeks olarak belirlediğimiz copy_data verisinden kullanıcı tarafından girilen besinin satırına erişme
new_data

"""# **5.GRAFİK OLUŞTURMA AŞAMASI**"""

#Kullanıcı tarafından girilen besinin dairesel grafiği
new_data.plot.pie(subplots = True ,figsize = (20,15),autopct = '%1.2f%%' , textprops={'fontsize': 10})

"""# **VERİLER İÇERİSİNDEKİ YAĞ KOLONUNUN SAYI DEĞERLERİNE GÖRE DAĞILIMININ GÖRSELLEŞTİRİLMESİ**"""

data['YAG(g)'].describe() #"YAG(g)" kolonunun istatistikleri

data['YAG(g)'].value_counts() #Bu satır verinin NaN dışındaki değerleri sayısal olarak ne kadar içerdiğini verir

#en yüksek yağ değerine sahip 18 besin
data['YAG(g)']=data['YAG(g)'].astype('category')
yag = data.sort_values(by=['YAG(g)'],ascending=False, na_position='last').head(18)

x_yag = yag.iloc[:,0:1]
x_yag = x_yag.astype(np.str)

y_yag = yag.iloc[:,4:5]
y_yag = y_yag.astype(np.float)

stack_yagmax = pd.concat([x_yag,y_yag],axis=0)

print(stack_yagmax)

#en yüksek yağ değerine sahip 18 besinin sütun grafiği
plt.figure(figsize=(32,5),facecolor='white')
sns.barplot(x= "BESINLER", y="YAG(g)", data=stack_yagmax )
plt.title("BESINLER ICERISINDEKI YAG MIKTARI")

#en düşük yağ değerine sahip 20 besin
data['YAG(g)']=data['YAG(g)'].astype('category')
yag = data.sort_values(by=['YAG(g)'],ascending=True).head(20)

x_yag = yag.iloc[:,0:1]
x_yag = x_yag.astype(np.str)

y_yag = yag.iloc[:,4:5]
y_yag = y_yag.astype(np.float)

stack_yagmin = pd.concat([x_yag,y_yag],axis=1)

print(stack_yagmin)

#en düşük yağ değerine sahip 20 besinin sütun grafiği
plt.figure(figsize=(35,5),facecolor='white')
sns.barplot(x= "BESINLER", y="YAG(g)", data=stack_yagmin )
plt.title("BESINLER ICERISINDEKI YAG MIKTARI")

stack_yag['YAG(g)'].plot.pie(subplots = True, labels= stack_yag['BESINLER'] ,figsize = (15,15),autopct = '%1.2f%%' , textprops={'fontsize': 10})

"""# **VERİLER İÇERİSİNDEKİ PROTEİN KOLONUNUN SAYI DEĞERLERİNE GÖRE DAĞILIMININ GÖRSELLEŞTİRİLMESİ**"""

data['PROTEIN(g)'].describe() #"PROTEIN(g)" kolonunun istatistikleri

data['PROTEIN(g)'].value_counts() #Bu satır verinin NaN dışındaki değerleri sayısal olarak ne kadar içerdiğini verir

#en yüksek protein değerine sahip 20 besin
data['PROTEIN(g)']=data['PROTEIN(g)'].astype('category')
protein = data.sort_values(by=['PROTEIN(g)'], ascending=False, na_position='last').head(20)  

x_protein = protein.iloc[:,0:1]


y_protein = protein.iloc[:,3:4]
y_protein = y_protein.astype(np.float)

stack_protein = pd.concat([x_protein,y_protein],axis=1)

print(stack_protein)

#en yüksek protein değerine sahip 20 besinin sütun grafiği
plt.figure(figsize=(35,7),facecolor='white')
sns.barplot(x= "BESINLER", y="PROTEIN(g)", data=stack_protein  )
plt.title("BESINLER ICERISINDEKI PROTEIN MIKTARI")

stack_protein['PROTEIN(g)'].plot.pie(subplots = True ,labels = stack_protein['      BESINLER'] ,figsize = (15,15) , autopct = '%1.2f%%' )

"""# **VERİLER İÇERİSİNDEKİ KARBONHİDRAT KOLONUNUN SAYI DEĞERLERİNE GÖRE DAĞILIMININ GÖRSELLEŞTİRİLMESİ**"""

data['KARBONHIDRAT(g)'].describe() #"KARBONHIDRAT(g)" kolonunun istatistikleri

data['KARBONHIDRAT(g)'].value_counts() #Bu satır verinin NaN dışındaki değerleri sayısal olarak ne kadar içerdiğini verir

#en yüksek karbonhidrat değerine sahip 20 besin
data['KARBONHIDRAT(g)']=data['KARBONHIDRAT(g)'].astype('category')
karbonhidrat = data.sort_values(by=['KARBONHIDRAT(g)'],na_position='last',ascending=False).head(20)

x_karbonhidrat = karbonhidrat.iloc[:,0:1]
x_karbonhidrat = x_karbonhidrat.astype(np.str)

y_karbonhidrat = karbonhidrat.iloc[:,5:6]
y_karbonhidrat = y_karbonhidrat.astype(np.float)

stack_karbonhidrat = pd.concat([x_karbonhidrat,y_karbonhidrat],axis=1)

print(stack_karbonhidrat)

#en yüksek karbonhidrat değerine sahip 20 besinin sütun grafiği
plt.figure(figsize=(40,7),facecolor='white')

sns.barplot(x="BESINLER", y="KARBONHIDRAT(g)", data=stack_karbonhidrat  )
plt.title("BESINLER ICERISINDEKI KARBONHIDRAT MIKTARI")

stack_karbonhidrat['KARBONHIDRAT(g)'].plot.pie(subplots = True ,labels = stack_karbonhidrat['BESINLER'] ,figsize = (15,30),autopct = '%1.2f%%' )

"""# 6.DİYET PROGRAMI HAZIRLANIŞI
 Her yaş grubunun alması gereken günlük enerji (kkal bakımından) belirlidir. Öncelik bunların belirlenmesi ardından da karbonhidrat , protein ve yağ bakımından yemek listesi hazırlanır.

# ÖNCELİKLE YAŞ - ENERJİ TABLOMUZU İNCELEYELİM
"""

yas_enerji

yas_enerji.describe() #yaş-enerji tablosunun istatistiği

yas_enerji.columns #yaş-enerji tablosunun kolonları

"""# **KULLANICIDAN İSTENİLEN YAŞ ARALIĞINA KARŞILIK GELEN GÜNLÜK ALMASI GEREKEN ENERJİYİ BULMA KISMI**"""

result = []


key = input("Günlük alınması gereken enerjiyi bulmak için cinsiyet(cinsiyet belirtilmek istenirse) ve yaş aralığını giriniz..:")

with open("yas_enerji.csv" , encoding='Latin-1') as csv_file:
  for satir in csv_file:
    if key in satir:
      result.append(satir.split(',')[0:])
          
          
print('Günlük alması gereken kalori bakımından enerji = ',result[:])

#Kullanıcı tarafından girilen bir yaş aralığının günlük alması gereken enerji miktarını veren kod 
yas = yas_enerji.set_index('YAS') #yas_enerji'nin içeriğini "YAS" sütununu index olacak şekilde yas'a kopyalıyoruz
yas_input = input("Yas aralıgınız : ") 
kkal = yas.loc[yas_input] 
kkal

gram = kkal["G.ENERJI(kkal)"]
gram / 4

"""# **YAŞ -ENERJİ BAKIMINDAN İLİŞKİLERİ GÖZLEMLEYEBİLMEK İÇİN GRAFİKLEŞTİRME AŞAMASI**"""

plt.figure(figsize=(30,6),facecolor='white')
sns.barplot(x='YAS', y='G.ENERJI(kkal)', data=yas_enerji)
plt.title("YAŞLARA GÖRE GÜNLÜK ALINMASI GEREKEN ENERJİ MİKTARLARI")

yas_enerji['G.ENERJI(kkal)'].plot.pie(subplots = True ,labels = yas_enerji['G.ENERJI(kkal)'] ,figsize = (10,10),fontsize = 10 , autopct = '%1.2f%%' )

"""# ENERJİ BAŞINA GÜNLÜK ALINMASI GEREKEN ENERJİNİN KARBONHİDRAT , PROTEİN VE YAĞ BESİN TÜRÜNE GÖRE DAĞILIMI ;
  

1.   %60 Karbonhidrat (kkal/4)
2.   %15 Protein (kkal/4)
3.   %25 Yağ (kkal/9)


Örnek: 

*   2250 kkal günlük enerji ihtiyacı : (grama dönüştür (kkal/4)
*   337.5 g Karbonhidrat
*   84.4 g Protein
*   62.5 g Yağ 
"""