"""

U2:
Account nomli class yarating.
Unda quyidagi rasmda ko`rsatilingan 
atrbut va methodlarni yaratinh.

"""

#code

class Account:
    """For Users' account and managing them"""
    def __init__(self,id : str ,name : str ,balance = 0):
        self.id = id
        self.name = name
        self.balance = balance

    def get_id(self):
        """Return ID"""
        return self.id

    def get_name(self):
        """Return Name"""
        return self.name
    
    def get_balance(self):
        """Return Balance"""
        return f"Balance:{self.balance}"
    
    def credit(self,amount : int):
        """Taking Cretids"""
        self.balance += amount
        return f"Finall Balance:{self.balance}"
    
    def debit(self,amount : int):
        """Debit your money"""
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Mablag` yetarli emas")
        return f"Finall Balance:{self.balance}"
    
    def transferTo(self,another,amount : int):
        """Transfer Money to Someone"""
        if amount <= self.balance:
            another.balance += amount
            self.balance -= amount
        else:
            print("Mablag` yetarli emas")

        return f"Finall Balance:{self.balance}"

    def toString(self):
        """Account to String"""
        return f"\nAccount:[id:{self.id}, name:{self.name}, balance:{self.balance}]"


#MAIN
user1 = Account("1234ABC","Ali",2000)    
user2 = Account("1R4G4C","Vali",0) 
user3 = Account("1RS4A5C","Aziz",1500) 
print()
print(user1.debit(100))
print(user1.transferTo(user2,200))
print(user1.toString())
print(user2.toString())
print()