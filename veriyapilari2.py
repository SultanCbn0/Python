#SET(KÜME) OLUŞTURMA
"""
s = set()

l=[1,"a","ali",123]
s=set(l)
s

t=("a","ali")
s1=set(t)
s1

ali="lütfen_ata_bakma_uzaya_git"

s2=set(ali)
s2

l=["ali","lütfen","ata","bakma","uzaya","git","git","ali","git"]

s3=set(l)
s3
len(s3)
l[0]
#s3[0] çalışmaz çünkü sıralı değil indexi yok
"""
#eleman ekleme çıkarma

l=["gelecegi","yazanlar"]

s=set(l)
s
s.add("ile")
s.add("gelecege_git")
s
s.remove("ile")

#####SETLER-Klasik küme işlemleri

# =============================================================================
# difference() ya da "-" ifadesi ile iki kümenin farkını alırız
# intersection() yada "&" ifadesi ile iki küme kesişimi
# union() ile iki kümenin birleşimi
# symmetric_difference() ikisindede olmayanları
# =============================================================================

#difference
set1= set([1,3,5])
set2= set([1,2,3])

set1.difference(set2)
set2.difference(set1)
set1.symmetric_difference(set2)

#intersection &union

set1.intersection(set2)
set2&set1

set1.union(set2)
set1.intersection_update(set2) 
set1

###SETLERDE SORGU İŞLEMLERİ

set1=set([7,8,9])
set=set([5,6,7,8,9,10])

#iki kümenin kesişiminin boş olup olmadıgının sorgulanması

set1.isdisjoint(set2)

#bir kümenin bütün elemanlarının başka bir küme içerisinde yer alıp almadığı 

set1.issubset(set2)#set1 set2 nin alt kümesi midir

#bir kümenin diğer kümeyi kapsayıp kapsamadığı

set2.issuperset(set1)






