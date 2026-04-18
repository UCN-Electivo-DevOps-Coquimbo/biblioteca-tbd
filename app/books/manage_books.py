import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "libros.json")

def get_books():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def create_book():
    print("\nCrear Libro")
    title = input("Título: ").strip()
    author = input("Autor: ").strip()
    editorial = input("Editorial: ").strip()
    year = input("Año: ").strip()
    genre = input("Género: ").strip()
    total_copies = input("Copias Totales: ").strip()

    books = get_books()
    new_id = max((b["id"] for b in books), default=0) + 1

    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "editorial": editorial,
        "year": int(year),
        "genre": genre,
        "total_copies": int(total_copies),
        "available_copies": int(total_copies)
    }

    books.append(new_book)
    save_books(books)
    print(f"\nEl libro '{title}' se agregó correctamente.")

def list_books():
    books = get_books()
    if not books:
        print("\nNo hay libros registrados.")
        return
    print("\nLibros disponibles")
    for b in books:
        print(f"[{b['id']}] Título: {b['title']}, Autor: {b['author']}, Editorial: {b['editorial']}, Año: {b['year']}, Género: {b['genre']}, Copias Totales: {b['total_copies']}, Copias Disponibles: {b['available_copies']}")

def manage_books():
    while True:
        print("\nGestionar Libros")
        print("1. Ver todos los libros")
        print("2. Agregar libro")
        print("3. Volver")
        opcion = input("> ").strip()

        if opcion == "1":
            list_books()
        elif opcion == "2":
            create_book()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")
