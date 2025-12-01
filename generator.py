import Book
import random

# check_db(filename):
#   this function should open the database and check if each line is a valid Book object
#   if it is not it should return (false, OFFENDING LINE)
#   if it is, it should return (true, None)
#   ex: check_db("valid_db.txt") -> (true, None)
#   ex: check_db("invalid_db.txt") -> (false, "book94383 2.5 1.6 3.9 7")
def check_db(filename):
    pass

# query_for(filename, name=None, fantastical=None, historical=None, content=None, story=None):
#   takes the filename of the db and one or more of name, historical, fantastical, etc. and returns
#   an array of Book objects which match the given arguments
#   ex: query_for("db.txt", name="Harry Potter") -> [Book(...), Book(...), Book(...)]
def query_for(filename, name=None, fantastical=None, historical=None, content=None, story=None):
    pass

# remove_entry(filename, book):
#   removes the db entry matching the book object from the db
#   returns true if it was successful
#   returns false on error or if the entry does not exist
def remove_entry(filename, book:Book.Book):
    pass


############ HELPER FUNCTIONS -- THESE SHOULD BE LEFT ALONE ######################

# add_entry(filename, book):
#   adds a db entry matching the book object from the db
#   returns true 
def add_entry(filename, book:Book.Book):
    with open(filename, "a") as f:
        f.write(f"{book.to_string()}\n")

# generate_db(filename, num_books):
#   generate a random correct db with a series of random books inside it
def generate_db(filename, num_books):
    for i in range(num_books):
        fantastical = random.randrange(1, 5)
        historical = random.randrange(1, 5)
        content = random.randrange(1, 5)
        story = random.randrange(1, 5)
        name = f"book{i}"

        book = Book.Book(name, fantastical, historical, content, story)

        add_entry(filename, book)

############ END HELPER FUNCTIONS -- THESE SHOULD BE LEFT ALONE ##################
