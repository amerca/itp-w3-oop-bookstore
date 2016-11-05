class Bookstore(object):
    """Bookstore object; <name> and list for <books> and <authors>"""
    def __init__(self,name,books=None):
        """Initializes a bookstore with name, and an optional list of books"""
        self.name=name
        # None objects automatically return false? (Not apparently)
        if books is None:
            self.books=[]
        else:
            self.books=books
        self.authors=[]

    def add_author(self, author):
        """Adds an author to the bookstore"""
        self.authors.append(author)

    def add_book(self,book):
        """Adds a book to the bookstore"""
        self.books.append(book)
        # Add the author in case the author is not present
        if not book.author in self.authors:
            self.add_author(book.author)

    def get_books(self):
        """Returns a list of books in the bookstore"""
        return self.books
       
    def print_info(self):
        """Prints information about the contents"""
        print('----------\nname:{}\nbooks:{}\nauthors:{}'.format(self.name,self.books,self.authors))
        
    def search_books(self, title=None, author=None):
        """Searches books with optional parameters"""
        if (title == None) and (author == None):
            print('Invalid parameters')
        
        # To introduce case insensitive, make the input title all lowercase
        if title != None:
            title = title.lower()
            
        # Initialize output
        output = []
        
        # Eliminate cases if they are not valid
        for book in self.books:
            if title != None:
                if not title in book.title.lower():
                    continue
            if author != None:
                if not author == book.author:
                    continue
            output.append(book)
        return output


class Book(object):
    def __init__(self,a_title,author):
        self.title=a_title
        self.author = author
        author.books.append(self)

    def __repr__(self):
        return '<Book:%s>' % self.title




class Author(object):
    
    def __init__(self,name,country):
        self.name=name
        self.nationality=country
        self.books = []
        
    def get_books(self,):
        return self.books
        
    def __repr__(self):
        return '<Author:%s>' % self.name  