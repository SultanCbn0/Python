#FONKSİYONLARA GİRİŞ VE FOKSİYON OKURYAZARLIĞI

#print("a","b",sep="_")
#?print

#FONKSİYON YAZMA
'''
def kare_al(x):
    y=x**2
    print("Girilen sayının karesi: ",y)
    
kare_al(8)

def kare_al1(x):
    y=x**2
    print("Girilen sayı:"+ str(x) + ",Karesi: " + str(y))
    
kare_al1(5)

def carpma_islemi(x,y):
    a=x*y
    print(a)
    
carpma_islemi(5, 7)



#ÖN TANIMLI FONKSİYONLAR

def carpma_islemi(x=4,y=3):
    print(x*y)
    
carpma_islemi()

#Argümanların siralaması

carpma_islemi(y=4,x=6)

#return

def direk_hesap(isi,nem,sarj):
    return (isi+nem)/sarj

direk_hesap(25, 40, 70)*6

#LOCAL VE GLOBAL DEĞİŞKENLER
#bu x ve y global değişken
x=10
y=20

def topla(x,y):#local değişkenler
    return x+y

topla(5,4)

##LOCAL ETKİ ALANINDAN GLOBAL ETKİ ALANINI DEĞİŞTİRMEK
'''

x=[]

def eleman_ekle(y):
    x.append(y)
    print(str(y)+" ifadesi eklendi")
    
eleman_ekle(5)
eleman_ekle("ali")




