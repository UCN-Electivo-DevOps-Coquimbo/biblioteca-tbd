import json

def delete_study_room(study_room_id):
    with(open('study_rooms.json', 'r')) as file:
        study_rooms = json.load(file)
    
    filtered_rooms = []
    for room in study_rooms:
        if room['id'] != study_room_id:
            filtered_rooms.append(room)
    study_rooms = filtered_rooms
                
    with(open('study_rooms.json', 'w')) as file:        
        json.dump(study_rooms, file)
        
        
study_rooms = {}
print("¿Qué sala de estudio deseas eliminar?")
print("------------SALAS--------------")
for study_room in json.load(open('study_rooms.json', 'r')):
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

delete_study_room(study_room_id)
print("Sala de estudio  eliminada exitosamente.")