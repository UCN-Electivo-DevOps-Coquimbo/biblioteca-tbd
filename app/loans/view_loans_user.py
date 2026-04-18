import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH_LOANS = os.path.join(BASE_DIR, "data", "loans.json")
DATA_PATH_BOOKS = os.path.join(BASE_DIR, "data", "book.json")
DATA_PATH_USERS = os.path.join(BASE_DIR, "data", "users.json")

#funcion para cargar los archivos
def load_json_data(path):
    #abre el archivo en modo lectura y convierte el json en lista
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

    

def view_my_loans():
    #carga los archivos
    loans = load_json_data(DATA_PATH_LOANS)
    books = load_json_data(DATA_PATH_BOOKS)
    users_file  = load_json_data(DATA_PATH_USERS)
    #entrar a la lista de ususarios
    users_list = users_file.get("users", []) if users_file else []
    
    if not loans:
        print("No hay préstamos registrados.")
        return

    print("\n" + "="*50)
    print("       HISTÓRICO DE PRÉSTAMOS DETALLADO")
    print("="*50)

    #recorrer cada prestamo del json loans 
    for loan in loans:
        #el next se usa para buscar dentro de la lista con el id book/usuario
        libro = next((b for b in books if b["id"] == loan["book_id"]), None)
        usuario = next((u for u in users_list if u["id"] == loan["user_id"]), None)
        #si existe se coloca el nombre, de lo contrario no
        titulo_libro = libro["title"] if libro else "Libro no encontrado"
        autor_libro = libro["author"] if libro else "N/A"
        nombre_usuario = usuario["name"] if usuario else "Usuario no encontrado"
        
        print(f"ID Préstamo: {loan['id']}")
        print(f"Libro:    {titulo_libro} ({autor_libro})")
        print(f"Usuario:  {nombre_usuario}")
        print("-" * 50)