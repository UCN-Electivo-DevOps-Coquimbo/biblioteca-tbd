import json
import os

JSON_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'data',
    'study_rooms.json'
)

def add_study_room(file_path, new_room):
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            rooms = json.load(file)
        except:
            rooms = []

    if "id" not in new_room or "name" not in new_room or "capacity" not in new_room:
        return {"error": "missing data"}

    for room in rooms:
        if room["id"] == new_room["id"]:
            return {"error": "id already exists"}

    if not new_room["name"]:
        return {"error": "empty name"}

    if new_room["capacity"] <= 0:
        return {"error": "invalid capacity"}

    if "available" not in new_room:
        new_room["available"] = True

    rooms.append(new_room)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(rooms, file, indent=2, ensure_ascii=False)

    return new_room

def add_study_room_flow():
    print("Which study room do you want to add?")
    new_room = {
        "id": int(input("Enter the room ID: ")),
        "name": input("Enter the room name: "),
        "capacity": int(input("Enter the room capacity: "))
    }

    result = add_study_room(JSON_FILE, new_room)
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("Study room added successfully.")