import json
import os

JSON_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'data',
    'study_rooms.json'
)

def delete_study_room(study_room_id):
    with open(JSON_FILE, 'r') as file:
        study_rooms = json.load(file)
    
    filtered_rooms = []
    for room in study_rooms:
        if room['id'] != study_room_id:
            filtered_rooms.append(room)
    study_rooms = filtered_rooms
                
    with open(JSON_FILE, 'w') as file:        
        json.dump(study_rooms, file)
        

def delete_study_room_flow():
    study_rooms = {}
    print("Which study room do you want to delete?")
    print("------------ROOMS--------------")
    for study_room in json.load(open(JSON_FILE, 'r')):
        print(f"ID: {study_room['id']}, Name: {study_room['name']}, Capacity: {study_room['capacity']}")
        study_rooms[study_room['id']] = study_room
        
    while True:
        study_room_id_input = input("Enter the room ID: ")
        if not study_room_id_input:
            print("ID is required.")
        if int(study_room_id_input) not in study_rooms:
            print("ID not found.")
        else:
            break
    study_room_id = int(study_room_id_input)

    delete_study_room(study_room_id)
    print("Study room deleted successfully.")