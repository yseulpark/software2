class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,name,author,page):
        super().__init__(name)
        self.author = author
        self.page = page
    def print_info(self):
        print(f"The book \"{self.name}\" has {self.page} pages and it is written by {self.author}.")

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_info(self):
        print(f"The magazine {self.name}'s chief editor is {self.chief_editor}.")
donald_duck = Magazine("Donald Duck","Aki Hyyppä")
compartment_no6= Book("Compartment No. 6","Rosa Liksom", 192)
donald_duck.print_info()
compartment_no6.print_info()

