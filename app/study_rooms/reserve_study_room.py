import json
import os

JSON_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'study_rooms.json')

def translate_availability(available):
    return "Sí" if available else "No"

def reserve_study_room(study_room_id):
    with(open(JSON_FILE, 'r')) as file:
        study_rooms = json.load(file)
    
    for study_room in study_rooms:
        if study_room['id'] == study_room_id:
            if not study_room.get('available', True):
                return "Sala no disponible"
            study_room['available'] = False
                
    with(open(JSON_FILE, 'w')) as file:        
        json.dump(study_rooms, file)

def reserve_study_room_flow():
    study_rooms = {}
    print("¿Qué sala de estudio deseas reservar?")
    print("------------SALAS--------------")
    for study_room in json.load(open(JSON_FILE, 'r')):
        print(f"ID: {study_room['id']}, Nombre: {study_room['name']}, Capacidad: {study_room['capacity']}, Disponible: {translate_availability(study_room['available'])}")
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
    result = reserve_study_room(study_room_id)
    if result == "Sala no disponible":
        print(result)
    else:
        print("Sala de estudio reservada exitosamente.")
