class Book:
    # Note all proper rankings should be between 1 and 5 (inc)
    fantastical = -1
    historical = -1
    content = -1
    story = -1
    name = ""
    def __init__(self, name, fantastical, historical, content, story):
        self.name = name
        self.fantastical = fantastical
        self.historical = historical
        self.content = content
        self.story = story

    def to_string(self):
        return f"{self.name} {self.fantastical} {self.historical} {self.content} {self.story}"
    
    def equals(self, other):
        return (self.name == other.name and
                self.fantastical == other.fantastical and
                self.historical == other.historical and
                self.content == other.content and
                self.story == other.story)

def book_from_string(str):
    str = str.split(" ")
    return Book(str[0], float(str[1]), float(str[2]), float(str[3]), float(str[4]))