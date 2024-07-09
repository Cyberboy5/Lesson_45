"""
U7:

Mashina nomli class yarating. 
Ushbu classning elementlari nomi, 
turi (yengil, yuk avtomobili), narxi, ishlab_chiqarilgan_yili. 
Mashinaning malumot nomli methodi bor unda mashina xaqida malumot chiqib keladi. 
10 ta mashina xaqida malumot berilgan mashinalarni ishlab chiqarilgan yili bo’yicha saralab ekranga chop eting.
Mashinani narxi kiritilmaganda default 4.000$ qiymatni berib keting.
"""

# code

class Car:
    def __init__(self,name,car_type,release_year,price = 4000):
        self.name = name
        self.type = car_type
        self.year = release_year
        self.price = price


    def malumot(self):
        print(f"""
    Mashina nomi:{self.name}, 
    Mashina Turi:{self.type}, 
    Ishlab chiqarilgan yil:{self.year}, 
    Narxi:{self.price}$""")


car1 = Car("NSX",'Light',1993)
car2 = Car("Alero","Heavy",2002,28000)
car3 = Car("Prelude","Heavy",1993,60000)
car4 = Car("Navigator","Light",2006)
car5 = Car("Titan","Heavy",2012,55000)
car6 = Car("Cherokee","Heavy",2000,27000)
car7 = Car("Lanos","Light",1999,5000)
car8 = Car("Impreza","Light",2010,53000)
car9 = Car("MX-6","Heavy",1994,1500)
car10 = Car("Damas","Light",2015,10000)
    
cars = [car1,car2,car3,car4,car5,car6,car7,car8,car9,car10]

sorted_cars = sorted(cars, key=lambda car: car.year)


print("\n%20s"%("Car Information"))
for car in sorted_cars:
    car.malumot()









