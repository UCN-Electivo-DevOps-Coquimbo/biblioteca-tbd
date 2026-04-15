from operator import ne
import json


def add_study_room(file_path, new_room):
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            rooms = json.load(file)
        except:
            rooms = []

    if "id" not in new_room or "name" not in new_room or "capacity" not in new_room:
        return {"error": "faltan datos"}

    for room in rooms:
        if room["id"] == new_room["id"]:
            return {"error": "id ya existe"}

    if not new_room["name"]:
        return {"error": "nombre vacio"}

    if new_room["capacity"] <= 0:
        return {"error": "capacidad invalida"}

    if "available" not in new_room:
        new_room["available"] = True

    rooms.append(new_room)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(rooms, file, indent=2, ensure_ascii=False)

    return new_room

print("¿Qué sala de estudio deseas agregar?")
new_room = {
    "id": int(input("Ingrese el ID de la sala: ")),
    "name": input("Ingrese el nombre de la sala: "),
    "capacity": int(input("Ingrese la capacidad de la sala: "))
}

result = add_study_room('study_rooms.json', new_room)
if "error" in result:
    print(f"Error: {result['error']}")
else:
    print("Sala de estudio agregada exitosamente.")
    