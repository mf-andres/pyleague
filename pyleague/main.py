import json
from pathlib import Path

import typer

app = typer.Typer()


def ask_for_participants():
    participants = list()
    i = 0
    while True:
        participant = input(f"Insert participant {i} or type 'done' to continue: ")
        if participant == "":
            break
        if participant == "done":
            break
        else:
            participants.append(participant)
            i += 1

    number_of_participants = len(participants)
    if number_of_participants % 2 != 0:
        participants.append("No one")

    return participants


def get_project_root_path():
    return Path(__file__).parent.parent


def store_participants(participants):
    print("Storing participants ...")
    root = get_project_root_path()
    participants_file_path = root / "files" / "participants.json"
    with open(participants_file_path, "w") as participants_file:
        json.dump(participants, participants_file)


def generate_groups_per_day(participants):
    print("Generating groups per day")
    number_of_participants = len(participants)
    number_of_days = number_of_participants - 1

    fixed_player = participants[0]
    rotating_players = participants[1:]
    groups_per_day = list()
    for i in range(int(number_of_days)):
        group = [fixed_player] + rotating_players
        groups_per_day.append(group)
        rotating_players = [rotating_players[-1]] + rotating_players[:-1]
    return groups_per_day


def store_groups_per_day(groups_per_day):
    print("Storing groups per day")
    root = get_project_root_path()
    groups_per_day_file_path = root / "files" / "groups_per_day.json"
    with open(groups_per_day_file_path, "w") as groups_per_day_file:
        json.dump(groups_per_day, groups_per_day_file)


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


@app.command()
def init():
    # ask for participants
    participants = ask_for_participants()
    # store participants
    store_participants(participants)
    # generate groups per day
    groups_per_day = generate_groups_per_day(participants)
    # store groups per day
    store_groups_per_day(groups_per_day)
    # generate day pointer
    day_pointer = generate_day_pointer(participants)
    # store day pointer
    store_day_pointer(day_pointer)


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


def read_group(day_pointer):
    print("Reading group")
    root = get_project_root_path()
    groups_per_day_file_path = root / "files" / "groups_per_day.json"
    with open(groups_per_day_file_path, "r") as groups_per_day_file:
        groups_per_day = json.load(groups_per_day_file)
    group = groups_per_day[day_pointer[0]]
    return group


def print_day_and_group(day_pointer, group):
    number_of_participants = len(group)

    pairs = list()
    for i in range(int(number_of_participants / 2)):
        pairs.append(f"{group[i]} VS {group[-i - 1]}")

    print(f"Day: {day_pointer[0]}")
    print("")
    for pair in pairs:
        print(pair)


@app.command()
def previous():
    # read day pointer
    day_pointer = read_day_pointer()
    # modify day pointer
    day_pointer = modify_day_pointer(day_pointer, next=False)
    # store modified day pointer
    store_day_pointer(day_pointer)
    # read corresponding group
    group = read_group(day_pointer)
    # print corresponding day and group
    print_day_and_group(day_pointer, group)


@app.command()
def today():
    # read day pointer
    day_pointer = read_day_pointer()
    # read corresponding group
    group = read_group(day_pointer)
    # print corresponding day and group
    print_day_and_group(day_pointer, group)


@app.command()
def next():
    # read day pointer
    day_pointer = read_day_pointer()
    # modify day pointer
    day_pointer = modify_day_pointer(day_pointer, next=True)
    # store modified day pointer
    store_day_pointer(day_pointer)
    # read corresponding group
    group = read_group(day_pointer)
    # print corresponding day and group
    print_day_and_group(day_pointer, group)


def read_participants():
    print("Reading participants ...")
    root = get_project_root_path()
    participants_file_path = root / "files" / "participants.json"
    with open(participants_file_path, "r") as participants_file:
        participants = json.load(participants_file)
    return participants


def print_participants(participants):
    print("Participants: ")
    for participant in participants:
        print(participant)


@app.command()
def participants():
    # read participants
    participants = read_participants()
    # print participants
    print_participants(participants)


if __name__ == "__main__":
    app()
