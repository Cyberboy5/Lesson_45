"""
U3:
Time nomli class yarating va quyidagi rasmda ko`rsatilgan atribut va methodlar ni yarating 
"""

#code

class Time:
    def __init__(self,hour : int,minute : int,second : int ) -> None:
        self.hour  = hour
        self.minute = minute
        self.second = second

#GETTERS
    def get_hour(self):
        return f"Hour:{self.hour}"
    
    def get_minute(self):
        return f"Minute:{self.minute}"
    
    def get_second(self):
        return f"Second:{self.second}"

#SETTERS
    def set_hour(self,new_hour):
        self.hour = new_hour

    def set_minute(self,new_minute):
        self.minute = new_minute

    def set_second(self,new_second):
        self.second = new_second

    def set_TIME(self,new_hour,new_minute,new_second):
        """Update data"""
        self.hour = new_hour
        self.minute = new_minute
        self.second = new_second

    def ToString(self):
        return (f"\nTime:{self.hour:02d}:{self.minute:02d}:{self.second:02d}\n")
    
    def nextSecond(self):
        if self.second == 59:
            self.second = 0
            if self.minute == 59:
                self.minute = 0
                self.hour +=1
            else:    
                self.minute += 1
        else:
            self.second +=1

    def previousSecond(self):

        if self.hour == 0 and self.minute == 0 and self.second == 0:
            self.hour = 23
            self.minute = 59
            self.second = 59
       
        elif self.second == 0 and self.minute == 0:
            self.second = 59
            self.minute = 59
            self.hour -=1
    
        elif self.second == 0:
            self.minute -= 1 
            self.second = 59

        else:    
            self.second -=1

        return self.ToString()


#MAIN
#input validationni tekshirish uchun alohida oldim
hour = int(int(input("\nEnter The Hour:")))
minute = int(int(input("Enter The Minute:")))
second = int(int(input("Enter The Second:")))

try:
    if not (0 <= hour <= 23 and  0 <= minute <= 59 and 0 <= second <= 59):
        raise print("Invalid Time!")
except:
    exit(1)

date1 = Time(hour,minute,second)

date1.nextSecond()

print(date1.ToString())