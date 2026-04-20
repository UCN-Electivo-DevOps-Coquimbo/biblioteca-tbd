import json
import os

def itsOption(x, opciones: list[str], check_type = str):
    # la funcion valida si x es una opcion valida al usar input(), dependiendo del tipo de dato esperado
    # x : cualquier cosa que es retornada por input()
    # opciones : lista de opciones a validar
    # type : tipo de dato esperado, por defecto es string, pero se puede cambiar a int u otro tipo
 
    if (x in opciones):
        if(check_type == int):
            if (x.isdigit()):
                return True
        elif (check_type == str):
            if(isinstance(x, str)):
                return True
        elif (check_type == float):
            try:
                float(x)
                return True
            except ValueError:
                return False
    return False


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Data paths
DATA_PATH_LOANS = os.path.join(DATA_DIR, "loans.json")
DATA_PATH_USERS = os.path.join(DATA_DIR, "users.json")
DATA_PATH_BOOKS = os.path.join(DATA_DIR, "book.json")


def get_data_path(file_name: str):
    return os.path.join(DATA_DIR, file_name)


def load_json_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
