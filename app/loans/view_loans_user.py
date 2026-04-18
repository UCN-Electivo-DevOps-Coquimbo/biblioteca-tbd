import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "loans.json")

def get_loans():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
    

def view_my_loans():
    my_loans = get_loans()
    print(my_loans)