# CFG'ye dil ağacı üretme

#Dallanma olan eleman ve içindeki pozisyon numarası
de = 0
dp = 0
dallanmavar = 1

##def DallanmaVarmi():
##    global de, dp, dallanmavar
##    # tumagac list'i ve Esyalar dict'i mutable olduğu için
##    # zaten global oluyor
##    boy = len(tumagac)
##    for i in range(boy):
##        deger = tumagac[i]
##        pozisyon = len(deger)
##        for j in range(pozisyon):
##            d = deger[j]
##            if d in Esyalar.keys():
##                de = i
##                dp = j
##                dallanmavar = 1
##                # print(de, dp, dallanmavar)
##                return True
##    dallanmavar = 0
##    return False

def DallanmaVarmi():
    
    # tumagac list'i ve Esyalar dict'i global olduğu için
    # bu fonksiyon içinden okunabiliyor.
    # bu fonksiyon içinde tanımlanan boy, i, deger, pozisyon, j, d,
    # de, dp, dallanmavar değişkenlerinin tamamı local değişkenlerdir.
    boy = len(tumagac)
    for i in range(boy):
        deger = tumagac[i]
        pozisyon = len(deger)
        for j in range(pozisyon):
            d = deger[j]
            if d in sozluk.keys():
                de = i
                dp = j
                dallanmavar = 1
                #print(de, dp, dallanmavar)
                
                break
        else:
            # j bitmiş. i'i dönmeye devam et
            continue

        # üstten yani j içinden break ile gelinmişse, i'i de break et.
        break
    else:
        # i döngüsü de bitmiş.
        dallanmavar, de, dp = 0, 0, 0


    # buraya ya break break'le gelinir veya son else işlendikten sonra gelinir.
    #print('return öncesi:',de, dp, dallanmavar)
    return (dallanmavar, de, dp)


#cfg'yi okutalım.
#cfg = input("CFG'i giriniz( |:Ayraç -->:Sağa ok ,:satır ayracı):")
cfg = "S-->aa|bX|aXX,X-->ab|b"
#cfg = "S-->aa|bX|aXX|aZ,X-->ab|b,Z-->a|bb"
#cfg = "S-->aa|bX|aXX|aZ,X-->ab|b|Zb,Z-->a|bb"

#Satırları ayıralım
k=cfg.split(',')
print('SATIRLAR:',k)

#Alt kümeleri oluşturalım
ilk = True
giris = ''
sozluk = {}
for i in k:
    degisken, degerler = i.split('-->')
    print('Degisken:',degisken,'Degerleri:',degerler)
    sozluk[degisken]=degerler.split('|')

    if ilk == True: giris = degisken ; ilk = False

print('-'*len('Sözlük: '+repr(sozluk)))
print('Sözlük:',sozluk)
print('-'*len('Sözlük: '+repr(sozluk)))

#Tum dil ağacı icin girişten başlayalım
tumagac = sozluk[giris]

maxdongu = 100
for dongusay in range(maxdongu):

    print('TÜM AĞAÇ:',tumagac)
    
    dallanmavar, de, dp = DallanmaVarmi()
    #print('Dönenler:',de, dp, dallanmavar)
    
    if dallanmavar == 1:
        eleman = tumagac[de]
        elemansol, elemansag = eleman[:dp], eleman[dp+1:]
        # print(elemansol, elemansag)
        
        altdallar = []
        altdal = tumagac[de][dp]
        for dal in sozluk[altdal]:
            altdallar.append(elemansol + dal + elemansag)

        # Altdalı olan eleman silinip, alt dalları yerleştirilecek.
        tumagac[de:de+1] = altdallar
    else:
        # Dallanma olmadığı için artık döngüye gerek yok
        break
else:
    print()
    print('*** HATA VAR *** ')
    print('{} KEZ DALLANMA YAPILDIĞI HALDE DALLANMA TAMAMLANAMADI !!!!!!'.format(maxdongu))
    

        

print('-'*len('TÜM AĞAÇ: '+repr(tumagac)))
# Tum ağacın içindeki birden fazla kayıtların ayıklanması
uretilenkelimeler = list(set(tumagac))
uretilenkelimeler.sort()
print('ÜRETİLEN KELİMELER:', uretilenkelimeler)

#Tekrarlanan kelimelerin bulunması
tekrarlanankelimeler = tumagac.copy()
#tumagac'dan üretilen kelimeler çıkartılarak, tekrarlanan kelimeler bulunacak
for i in uretilenkelimeler:
    tekrarlanankelimeler.remove(i)

#tekrarlanan kelimelerin birden fazla ise teke indirilmesi
tekrarlanankelimeler = list(set(tekrarlanankelimeler))
tekrarlanankelimeler.sort()
print('TEKRARLANAN KELİMELER:', tekrarlanankelimeler)

##maxdongu = 100
##dongusay = 0
##while dallanmavar == 1 and dongusay < maxdongu:
##
##    dongusay += 1
##    print('TÜM AĞAÇ:',tumagac)
##    
##    dallanmavar, de, dp = DallanmaVarmi()
##    #print('Dönenler:',de, dp, dallanmavar)
##    
##    if dallanmavar == 1:
##        eleman = tumagac[de]
##        elemansol, elemansag = eleman[:dp], eleman[dp+1:]
##        # print(elemansol, elemansag)
##        
##        altdallar = []
##        altdal = tumagac[de][dp]
##        for dal in Esyalar[altdal]:
##            altdallar.append(elemansol + dal + elemansag)
##
##        # Altdalı olan eleman silinip, alt dalları yerleştirilecek.
##        '''
##        tumagac.pop(de)
##        altdallar.reverse()
##        for dal in altdallar:
##            tumagac.insert(de, dal)
##        '''
##    
##        tumagac[de:de+1] = altdallar
##
##        
##
##print('-'*len('TÜM AĞAÇ: '+repr(tumagac)))
### Tum ağacın içindeki birden fazla kayıtların ayıklanması
##uretilenkelimeler = list(set(tumagac))
##uretilenkelimeler.sort()
##print('ÜRETİLEN KELİMELER:', uretilenkelimeler)
##
###Tekrarlanan kelimelerin bulunması
##tekrarlanankelimeler = tumagac.copy()
###tumagac'dan üretilen kelimeler çıkartılarak, tekrarlanan kelimeler bulunacak
##for i in uretilenkelimeler:
##    tekrarlanankelimeler.remove(i)
##
###tekrarlanan kelimelerin birden fazla ise teke indirilmesi
##tekrarlanankelimeler = list(set(tekrarlanankelimeler))
##tekrarlanankelimeler.sort()
##print('TEKRARLANAN KELİMELER:', tekrarlanankelimeler)
##
##if dongusay == maxdongu:
##    print()
##    print('*** HATA VAR *** ')
##    print('{} KEZ DALLANMA YAPILDIĞI HALDE DALLANMA TAMAMLANAMADI !!!!!!'.format(maxdongu))
    
