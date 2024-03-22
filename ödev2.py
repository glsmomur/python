# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

fibonacci = [1, 1]  

while len(fibonacci) < 20:  
    next_fib = fibonacci[-1] + fibonacci[-2]  
    fibonacci.append(next_fib)

print("En az 20 elemanlı Fibonacci serisi: ", fibonacci)


fibonacci_serisi = [1, 1]

while len(fibonacci_serisi) < 20:
    son_eleman = fibonacci_serisi[-1]
    bir_onceki_eleman = fibonacci_serisi[-2]
    yeni_eleman = son_eleman + bir_onceki_eleman
    fibonacci_serisi.append(yeni_eleman)

print("Fibonacci Serisi: ", fibonacci_serisi)

# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.

def mukemmel_sayi_mi(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    return toplam == sayi

sayi = int(input("Bir sayı girin: "))

if mukemmel_sayi_mi(sayi):
    print(sayi, "bir mükemmel sayıdır.")
else:
    print(sayi, "bir mükemmel sayı değildir.")

# 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız. 
    
def ebob_bul(sayi1, sayi2):
    while sayi2 != 0:
        sayi1, sayi2 = sayi2, sayi1 % sayi2
    return sayi1

def ekok_bul(sayi1, sayi2):
    return sayi1 * sayi2 // ebob_bul(sayi1, sayi2)

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

ebob = ebob_bul(sayi1, sayi2)
ekok = ekok_bul(sayi1, sayi2)

print("Girilen sayıların EBOB'u:", ebob)
print("Girilen sayıların EKOK'u:", ekok)

# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

def asal_mi(sayi):
    if sayi <= 1:
        return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True

sayi = int(input("Bir sayı girin: "))

if asal_mi(sayi):
    print(sayi, "bir asal sayıdır.")
else:
    print(sayi, "bir asal sayı değildir.") 


#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

def asal_carpans(sayi):
    carpanlar = []
    carpan = 2
    
    while sayi > 1:
        if sayi % carpan == 0:
            carpanlar.append(carpan)
            sayi //= carpan
        else:
            carpan += 1
    
    return carpanlar

sayi = int(input("Bir sayı girin: "))
print(f"{sayi} sayısının asal çarpanları: {asal_carpans(sayi)}") 