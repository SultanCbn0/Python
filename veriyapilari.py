#Veri Yapıları
"""
#######Listeler
#[]
#list()

notlar=[90,80,70,50]
type(notlar)

liste=["a", 10,20,30]
liste2=["b",50,[15,4,6],liste]

type(liste2[0])

liste[:2]
liste[0:]

liste2[2][1]
#del liste2

##################      

liste=["ali","veli","berkcan","ayse","ali","berkcan"]

#append sona ekler
liste.append("berkcan")

#remove siler
liste.remove("berkcan")

#insert verilen indexe ekler
liste.insert(0,"fatma")
liste.insert(len(liste),"beren")

#pop siler ekrana basar

liste.pop(0)

#count verilen ifadeyi sayar
liste.count("ali")

#copy listeyi kopyalar

yedek=liste.copy()

#extend liste birleştirme

liste.extend(["a","b",10])

#index verilen indexteki ifadeyi getirir

liste.index("ali")

#reverse listeyi tersine çevirir
liste.reverse()

#sort sıralama
liste2=[10,45,85,5]
liste2.sort()

#clear
liste2.clear()
"""
####TUPLE --değiştirilemezler

t=("ali","ayşe",1,5,8.7,[1,2,3,4])

t1="ali","ayşe",1,5,8.7,[1,2,3,4]

t2=("eleman",)#tek elemanlı tuple oluştururken sonuna "," at yoksa tuple olduğunu anlamaz
type(t2)

###Dictionary -sıralı değillerdir

sozluk={"REG" : "REGRESYON MODELİ",
        "LOJ" : "LOJİSTİK MODELİ",
        "CART": "CLASSIFICATION AND REG"}

sozluk
len(sozluk)

sozluk2={"REG" : ["RMSE",10],
        "LOJ" : ["MSE",20],
        "CART": ["SSE",30]}

sozluk["REG"]

sozluk2["REG"]

sozluk3={"REG" : {"RMSE":10,
                  "MSE" :20,
                  "SSE" :30},
        "LOJ"  : {"RMSE":10,
                  "MSE" :20,
                  "SSE" :30},
        "CART" : {"RMSE":10,
                  "MSE" :20,
                  "SSE" :30}}

sozluk3["REG"]["SSE"]

#eleman ekleme ve değiştirme

sozluk["GBM"]="GRADIENT BOOSTING MAC"
sozluk

sozluk["REG"]="COKLU DOGRUSAL REGRESYON"


