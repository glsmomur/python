def muhtesem_sayi_mi(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    return toplam == sayi

sayi = int(input("Bir sayı girin: "))

if muhtesem_sayi_mi(sayi):
    print(sayi, "bir muhteşem sayıdır.")
else:
    print(sayi, "bir muhteşem sayı değildir.")