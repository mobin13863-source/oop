# i want to use dunder method len

class Book():
    def __init__(self, name, page):
        self.name = name
        self.page = page

    def __len__(self):
        return (len(self.name))
      

b = Book("python", 334)

print(len(b))
