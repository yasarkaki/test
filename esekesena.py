print("VİZE FİNAL HESABI")
print("Vize Etkisi %40 , Final Etkisi %60 Olarak Belirlenmiştir")
print("Geçiş Notu 60 Olarak Belirlenmiştir")

vize = float(input("Vize notunuzu giriniz : "))
final = float(input("Final notunuzu giriniz : "))

k = ((vize*4)/10 + (final*6)/10)

if k >= 70:
    print("Tebrikler Geçtiniz! Ortalamanız : " , k)
else :
    print("Ortalamanız :" , k ,"Bütünleme Sınavı Tarihleri Sitemizde Açıklanacaktır")


