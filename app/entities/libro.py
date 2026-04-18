class Libro:
    def __init__(self, title, author, editorial, year, genre, available):
        self.title = title
        self.author = author
        self.editorial = editorial
        self.year = year
        self.genre = genre
        self.available = available

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Editorial: {self.editorial}, Year: {self.year}, Genre: {self.genre}, Available: {self.available}"