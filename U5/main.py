
"""
Rectangle nomli class yarating>Klass namumasi hight va width atributlarni qabul qiladi.
Rectangle class ida quyidagi methodlarni yarating.

"""

#code

class Rectangle:
    def __init__(self,hight,width):
        self.hight = hight
        self.width = width
    
    def get_hight(self):
        return self.hight
    
    def set_hight(self,new_hight):
        self.hight = new_hight

    def get_width(self):
        return self.width

    def set_width(self,new_width):
        self.width = new_width

    def get_area(self):
        return self.hight * self.width

    def get_perimeter(self):
        return (self.hight + self.width)*2
    
    def get_info(self):
        print(f"""
    Hight:{self.hight}
    Width:{self.width}
    Area:{self.get_area()}
    Perimeter:{self.get_perimeter()}""")
        

#MAIN
r1 = Rectangle(11,10)
r2 = Rectangle(25,12)
r3 = Rectangle(5,20)

r1.get_info()
print()