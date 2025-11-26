# i want to use dunder del

class Book():
    def __init__(self, name, page):
        self.names = name
        self.page = page

    def open(self):
        return f'the book {self.names} with {self.page} page'
    
    def __str__(self):
        return f'{self.names}, {self.page}'
    
    def __del__(self):
        print (f'ohh the Book {self.names} is over')
    
b = Book("python", 334)

del b

d = Book("nam", 445)

print(d.open())