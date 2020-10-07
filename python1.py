"""
    gel_yaz="*gelecegi_yazanlar*"
    
    #String Metodları len()
    len(gel_yaz)
    
    ############
    #upper() & lower()
    
    B=gel_yaz.upper()
    gel_yaz.lower()
    
    
    B.islower()
    B.isupper()
    
    #replace() yer değiştirme metodu 
    
    gel_yaz.replace("e", "a")
    
    #strip() istenmeyen stringleri kırpma
    
    #gel_yaz.strip()#ön tanımlı olarak boşluk stringi var
    
    gel_yaz.strip("*")
    
    #dir() verilen değişkende hangi mmetodları kullanabileceğimizi gösterir
    
    dir(gel_yaz)
    
    #SUBSTRINGLER
    
    gel_yaz[5]
    gel_yaz[0:3]
"""
#type dönüşümleri

sayi1=input()
sayi2=input()
toplam=int(sayi1)+int(sayi2)
print(toplam)

#Print

print("sultan", "coban", sep = "_")#sep->iki kelime arasına sep'e verilen karakteri koyar











