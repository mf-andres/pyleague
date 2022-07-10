import json

from pyleague.path_utils import get_project_root_path


def generate_day_pointer(participants):
    print("Generating day pointer")
    number_of_participants = len(participants)
    number_of_days = number_of_participants - 1
    day_pointer = (0, number_of_days)
    return day_pointer


def store_day_pointer(day_pointer):
    print("Storing day pointer")
    root = get_project_root_path()
    day_pointer_path = root / "files" / "day_pointer.json"
    with open(day_pointer_path, "w") as day_pointer_file:
        json.dump(day_pointer, day_pointer_file)

def read_day_pointer():
    print("Reading day pointer")
    root = get_project_root_path()
    day_pointer_path = root / "files" / "day_pointer.json"
    with open(day_pointer_path, "r") as day_pointer_file:
        day_pointer = json.load(day_pointer_file)
    return day_pointer


def modify_day_pointer(day_pointer, next):
    print("Modifying day pointer")
    if next:
        day_pointer[0] += 1
        day_pointer[0] %= 3
    else:
        day_pointer[0] += -1
        day_pointer[0] %= 3
    return day_pointer

