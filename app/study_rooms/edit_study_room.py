import json
import os

JSON_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'study_rooms.json')

def edit_study_room(study_room_id, new_name=None, new_capacity=None):
    with(open(JSON_FILE, 'r')) as file:
        study_rooms = json.load(file)
    
    for study_room in study_rooms:
        if study_room['id'] == study_room_id:
            if new_name:
                study_room['name'] = new_name
            if new_capacity:
                study_room['capacity'] = new_capacity
                
    with(open(JSON_FILE, 'w')) as file:        
        json.dump(study_rooms, file)
        
def edit_study_room_flow():       
    study_rooms = {}
    print("¿Qué sala de estudio deseas editar?")
    print("------------SALAS--------------")
    for study_room in json.load(open(JSON_FILE, 'r')):
        print(f"ID: {study_room['id']}, Nombre: {study_room['name']}, Capacidad: {study_room['capacity']}")
        study_rooms[study_room['id']] = study_room
        
    while True:
        study_room_id_input = input("Ingrese el ID de la sala: ")
        if not study_room_id_input:
            print("ID es obligatorio.")
        if int(study_room_id_input) not in study_rooms:
            print("ID no encontrado.")
        else:
            break
    study_room_id = int(study_room_id_input)

    new_name = input("Nuevo nombre (deja en blanco para no cambiar): ")

    while True:
        new_capacity_input = input("Nueva capacidad (deja en blanco para no cambiar): ")
        if new_capacity_input and not new_capacity_input.isdigit():
            print("Capacidad debe ser un número.")
        if new_capacity_input and int(new_capacity_input) <= 0:
            print("Capacidad debe ser mayor a 0.")
        else:
            break

    new_capacity = int(new_capacity_input) if new_capacity_input else None

    edit_study_room(study_room_id, new_name or None, new_capacity)
    print("Sala de estudio editada exitosamente.")

        