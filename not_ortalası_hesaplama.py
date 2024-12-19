#Not hesaplama sistemi
not1 = float(input("ilk sınav notu:"))
not2 = float(input("ikinci sınav notu:"))
not3 = float(input("ucuncu sınav notu"))

ortalama = (not1 + not2 + not3) / 3

print("ortalamanız:" , ortalama ) 

if ortalama >= 60 :
    print("tebrikssss gectin")
else :
    print("kaldın hacı ya")