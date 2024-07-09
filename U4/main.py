"""
U4:
Employee nomli class yarating va quyidagi rasmda ko`rsatilgan atribut va methodlar ni yarating 
"""

#code

class Employee:
    def __init__(self,ID : int,firstname : str,lastname : str,salary : int) -> None:
        self.id = ID
        self.fname = firstname
        self.lname = lastname
        self.salary = salary

    def get_id(self):
        return f"ID:{self.id}"
    
    def get_fname(self):
        return f"First Name:{self.fname}"
    
    def get_lname(self):
        return f"Last Name:{self.lname}"
    
    def get_name(self):
        return f"Fullname:{self.fname} {self.lname}"
    
    def get_salary(self):
        return f"Salary:{self.salary}"
    
    def set_salary(self,new_salary):
        self.salary = new_salary

    def get_AnnualSalary(self):
        self.salary *= 12
        return f"Salary:{self.salary}"
    
    def raise_salary(self,persentage):
        self.salary += (persentage / 100) * self.salary
        return f"Salary:{self.salary}"
    
    def ToString(self):
        return f"Emplayee:[ID:{self.id}, FullName:{self.fname} {self.lname}, Salary:{self.salary}]"


#MAIN
worker1 = Employee(1234,"Ali","Valiyev",1000)
worker2 = Employee(7369,"Aziz","Azizov",1200)
worker3 = Employee(14259,"Vali","Aliyev",800)

print()
print(worker1.get_name())
print(worker1.ToString())
print()