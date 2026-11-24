class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is not available.")

    def return_book(self):
        self.is_available = True
        print(self.title, "has been returned.")

    def show_info(self):
        print("Title:", self.title, "| Author:", self.author, "| Available:", self.is_available)


# Test
book1 = Book("Kürk Mantolu Madonna", "Sabahattin Ali")
book1.show_info()

book1.borrow()
book1.show_info()

book1.return_book()
book1.show_info()
