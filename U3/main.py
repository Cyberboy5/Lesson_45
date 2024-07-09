"""
U3:
Date nomli class yarating va quyidagi rasmda ko`rsatilgan atribut va methodlar ni yarating 
"""

#code

class Date:
    def __init__(self,day : int,month : int,year : int ) -> None:
        self.day  = day
        self.month = month
        self.year = year

#GETTERS
    def get_day(self):
        return f"Day:{self.day}"
    
    def get_month(self):
        return f"Month:{self.month}"
    
    def get_year(self):
        return f"Year:{self.year}"

#SETTERS
    def set_day(self,new_day):
        self.day = new_day

    def set_month(self,new_month):
        self.month = new_month

    def set_year(self,new_year):
        self.year = new_year

    def set_DATE(self,new_day,new_month,new_year):
        """Update data"""
        self.day = new_day
        self.month = new_month
        self.year = new_year

    def ToString(self):
        return (f"\nDate:{self.day :02d},{self.month :02d},{self.year}\n")
    

#MAIN
#input validationni tekshirish uchun alohida oldim
day = int(int(input("Enter The Day:")))
month = int(int(input("Enter The Month:")))
year = int(int(input("Enter The Year:")))

try:
    if not (1 <= day <= 31 and  1 <= month <= 12 and 1990 <= year <= 9999):
        raise print("Iltimos to`gri sana kiriting")
    
except:
    exit(1)



date1 = Date(day,month,year)
print(date1.ToString())
date1.set_day(12)
print(date1.ToString())