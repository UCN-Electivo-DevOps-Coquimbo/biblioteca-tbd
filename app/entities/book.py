class Book:
    def __init__(self, id, title, author, editorial, year, genre, total_copies, available_copies):
        self.id = id
        self.title = title
        self.author = author
        self.editorial = editorial
        self.year = year
        self.genre = genre
        self.total_copies = total_copies
        self.available_copies = available_copies

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "editorial": self.editorial,
            "year": self.year,
            "genre": self.genre,
            "total_copies": self.total_copies,
            "available_copies": self.available_copies
        }