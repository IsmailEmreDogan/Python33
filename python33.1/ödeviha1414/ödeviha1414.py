sayi=int(input("Bir sayı giriniz:"))
bölen=2
for i in range(1,sayi):
    if(sayi%bölen==0):
        print(bölen)
        sayi/=bölen
    else:
            bölen+=1




kelime=(input(" Bir kelime giriniz "))
kelimeuzunluğu= int(len(kelime))

for i in range(kelimeuzunluğu):
    sonuc=1
    sonuc =sonuc*(i+1)
print("Kelimenin faktöriyel olarak uzunluğu :  " ,(sonuc*i))
    




isimler=[]
vizeler=[]
finaller=[]
notOrt=[]
for i in range(2):
    isim=input("Öğrencinin ismini giriniz:  ")
    isimler.append(isim)
    vize=int(input("Ogrencinin vize notunu giriniz:  "))
    vizeler.append(vize)
    final=int(input("Ogrencinin final notunu giriniz:  "))
    finaller.append(final)
    ort=(vize*0.3) + (final*0.7)
    notOrt.append(ort)
    print( isimler[i]," isimli ogrencinin notları ",vizeler[i]," - ", finaller[i]," not ortalaması: ",notOrt[i])

    if (ort>=90):
        print(" Harf notu AA'dır ")
    elif (ort>=85):
        print(" Harf notu BA'dır ")
    elif (ort>=80):
        print(" Harf notu BB'dır ")
    elif (ort>=75):
        print( " Harf notu CB'dır ")
    elif (ort>=70):
        print( " Harf notu CC'dır ")
    elif (ort>=65):
        print( " Harf notu DC'dır ")
    elif (ort>=60):
        print( " Harf notu DD'dır ")
    elif (ort>=50):
        print( " Harf notu FD'dır ")
    else :
        print( " Harf notu FF'dır ")

      

     
