class Book():
    library_name = "mahabad_library" # make a attribute
    def __init__(self, title, author, year,genre):
        # Instance attribute with self for that I'll be direct and i use Direct that attribute
        self.title = title
        self.author = author   
        self.year = year
        self.genre = genre


    # make method info 
    def get_info(self):
        return f"title : {self.title}, author : {self.author}, year : {self.year}, genre : {self.genre}"
    

    # make method full_info for library_name
    def full_info(self):
        return f"title : {self.title}, author : {self.author}, year : {self.year}, genre : {self.genre} and name library is {Book.library_name}"
    


b = Book("learnig_python", "jadi", 2000,"teaching")
print(b.get_info())
print(b.full_info())
print('Book_class_is_over')


# i make seconed class for inheritance Book class
class Magazine(Book):
    def __init__(self, title, author, year,genre, issue_number):
        super().__init__(title, author, year, genre)
        self.issue_number = issue_number


    # override method get_info
    def get_info(self):
        return f"title : {self.title}, author : {self.author}, year : {self.year}, genre : {self.genre} and issue_number is {self.issue_number}"
    

    # make dunder or magic method 
    def __str__(self):
        return f'{self.title}, {self.author}, {self.year}, {self.genre}, {self.issue_number}'
    


m = Magazine("learnig_python", "jadi", 2000,"teaching", 3)
print(m)
print(m.get_info())

print() # I just want it to skip a blank line

#  i use Polymorphism 
for all in [b,m]:
    print(all.get_info())
    
