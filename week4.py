""""
how_much = int(input("How much money in your bank account? :"))
real_estate = int(input("How many houses do you have in Kötekli? :"))
car = (input("Do you have a car? :"))

threshold_money = 100000
threshold_house = 5

if how_much > threshold_money and real_estate > threshold_house :
    if car == "yes" or car == "Yes" :
        print("You don't have to all day work")
    else :
        print("You should buy a car")
elif how_much > 50000 and (car == "Yes" or car == "yes") :
    print("It is enough to work a day in a week")
else :
    print("You are so poor you have to work to live")
"""

car_hp = int(input("Enter car's hp :"))

if car_hp >= 150 and car_hp < 200 :
    print("1.200.00 tl")
elif car_hp >= 110 and car_hp < 150  :
    print("700.000 tl")
elif car_hp >= 90 and car_hp < 110 :
    print("500.00 tl")
elif car_hp >= 75 and car_hp < 90 :
    print("350.000 tl")
elif car_hp >= 60 and car_hp < 75 :
    print("200.000")
elif car_hp < 60 :
    print("For free")
else :
    print("2.000.000 tl")

