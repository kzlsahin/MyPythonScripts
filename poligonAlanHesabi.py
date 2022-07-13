
print("nokta koordinatları girmek için saat yönünde devam edip başlangıç noktasına \
tekrar dönecek şekilde her köşenin koordinatlarını x,y şeklinde virgül ile ayrılmmış \
olarak girin.\n Başlangıc ve bitiş koordinatları aynı olmalıdır.\
koordinatları girmek için: \n inputVertexes() \
alanı hesaplamak için: \n alanVer(a) \n   komutunu kullanın. \
('a' tanımlı değişkendir)")
def inputVertexes():
    b = 'Y'
    global a
    initialised = False
    while b != 'N' or b != 'n':
        b = input("Koordinat gir (örn. 0.0,0.0) veya bitirmek içi 'enter' veya, \'N\':\n")
        if b == 'N' or b == 'n' or b == '':
            break
        
        inputString = b.split(',')
        print(inputString[0]+"  "+inputString[1])
        inputVertex = [float(inputString[0]),float(inputString[1])]
        if not initialised:
            a = [inputVertex]
            initialised = True
        else:
            a = a + [inputVertex]
    return a

def alanVer(a=None):
    if a == None:
        a = inputVertexes()
    print("koordinatlar",a)
    toplam = 0
    for i in range(len(a)-1):
        toplam += (a[i+1][0]*a[i][1] - a[i][0]*a[i+1][1])/2
    return toplam
