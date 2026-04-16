import requests

def get_book(book):
    response = requests.get(f"http://openlibrary.org/search.json?title={book}")
    data = response.json()
    return data

def solicitar_prestamo_libro():
    book = ""
    while book == "":
        print("\n=== Préstamo de Libro ===")
        book = input("¿Qué libro desea buscar? ('c' para cancelar): ")
        if book.lower() == 'c':
            break
        
        data_obtained = get_book(book)
        libros = data_obtained.get("docs", [])
        
        if not libros:
            print(f"No se encontraron libros para '{book}'")
            book = ""
            continue

        page = 0
        items_per_page = 10
        seleccionado = False
        
        while not seleccionado:
            start_idx = page * items_per_page
            end_idx = start_idx + items_per_page
            current_libros = libros[start_idx:end_idx]
            
            print(f"\n--- Página {page + 1} de {(len(libros) + items_per_page - 1) // items_per_page} ({len(libros)} libros encontrados) ---")
            for i, lib in enumerate(current_libros):
                titulo = lib.get("title", "Sin título")
                autores = ", ".join(lib.get("author_name", ["Autor desconocido"]))
                print(f"[{start_idx + i + 1}] {titulo} (Autor: {autores})")
            
            print("\nOpciones:")
            if end_idx < len(libros):
                print("'s' -> Siguiente página")
            if page > 0:
                print("'a' -> Página anterior")
            print("'c' -> Cancelar búsqueda")
            print("Número del libro -> solicitar libro.")
            
            seleccion = input("> ").strip().lower()
            
            if seleccion == 's' and end_idx < len(libros):
                page += 1
            elif seleccion == 'a' and page > 0:
                page -= 1
            elif seleccion == 'c':
                print("Búsqueda cancelada.")
                break
            elif seleccion.isdigit():
                idx = int(seleccion) - 1
                if 0 <= idx < len(libros):
                    libro_req = libros[idx]
                    print(f"\nEl libro '{libro_req.get('title', 'Sin título')}' ha sido solicitado correctamente.")
                    seleccionado = True
                else:
                    print("Número de libro fuera de rango.")
            else:
                print("Opción inválida.")
