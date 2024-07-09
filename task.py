class Book:
    def __init__(self, title: str, author: str, publication_year: int):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title} by {self.author}, {self.publication_year}"

class User:
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.id = user_id

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.borrowed_books = {}

    def add_book(self, book: Book):
        self.books.append(book)
        return f"Kitob qo'shildi: {book}"

    def add_user(self, user: User):
        self.users.append(user)

    def borrow_book(self, kitob: Book, user: User):
        if kitob in self.books:
            self.books.remove(kitob)

            if user.id not in self.borrowed_books:
                self.borrowed_books[user.id] = [kitob]
                return f"{user.name} '{kitob.title}' ni oldi"
            else:
                self.borrowed_books[user.id].append(kitob)
                return f"Yana {user.name} yangi '{kitob.title}' ni oldi"
        else:
            print(self.borrowed_books)
            return "Kitob mavjud emas"

    def return_book(self, book_title: str, user: User):
        for book in self.borrowed_books.get(user.id, []):
            if book.title == book_title:
                self.borrowed_books[user.id].remove(book)
                self.books.append(book)
                return f"Kitob qaytarildi: '{book_title}'"
        return "Kitob topilmadi"

#books
book1 = Book('Python Programming', 'John Doe', 2000)
book2 = Book('Learning C++', 'Jane Smith', 1990)
book3 = Book("Moby Dick", 720, 18.99)
book4 = Book("The Great Gatsby", 180, 10.99)

#users
user1 = User('Alice', 123)
user2 = User('Bob', 456)

lib = Library()

print(lib.add_book(book1))
print(lib.add_book(book2))
print(lib.add_book(book3))
print(lib.add_book(book4))

lib.add_user(user1)
lib.add_user(user2)

print(lib.borrow_book(book1, user1))
print(lib.borrow_book(book2, user1))
print(lib.borrow_book(book3, user2))
print(lib.borrow_book(book4, user2))

print(lib.return_book('Python Programming', user1))
print(lib.return_book('Nonexistent Book', user1))
