def esOpcion(x, opciones: list[str], check_type = str):
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
