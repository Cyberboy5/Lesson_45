"""
U8:

Book nomli class yarating va uning property elementlari quyidagilardan iborat:

-        Name(Kitob nomi);
-        Page_count(Kitobning sahifalar soni);
-        Price(Kitobning narxi).
Ushbu classga tegishli 5ta obyekt yarating va ularni ma’lumotlarni foydalanuvchi tomonidan kiriting.

Sizning vazifangiz quyidagilardan iborat bo‘lgan har bir obyekt uchun metodlar yaratish:

1)    Barcha kitoblarning sahifalar sonini 10taga oshiring.
2)    Agar sahifalar soni 100tadan ko‘p bo‘lsa(oshirishdan keyin), ushbu kitobning narxini 2 barobar kamaytiring.
"""

#code

class Book:
    def __init__(self,name,page_count,price):
        self.name = name
        self.page = page_count
        self.price = price


    def add_10_pages(self):
        self.page +=10

    def price_decreasing(self):
        if self.page >= 100:
            self.price /=2
    
    def get_info(self):
        print(f"""
    Kitob nomi: {self.name}
    Sahifalar soni: {self.page}
    Narxi: {self.price}$""")


book1 = Book("To Kill a Mockingbird", 281, 15.99)
book2 = Book("1984", 328, 12.99)
book3 = Book("Moby Dick", 720, 18.99)
book4 = Book("The Great Gatsby", 180, 10.99)
book5 = Book("War and Peace", 1225, 22.99)

books = [book1, book2, book3, book4, book5]

for book in books:
    book.add_10_pages()
    book.price_decreasing()

for book in books:
    book.get_info()