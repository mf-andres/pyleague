import json

from pyleague.path_utils import get_project_root_path


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


def read_group(day_pointer):
    print("Reading group")
    root = get_project_root_path()
    groups_per_day_file_path = root / "files" / "groups_per_day.json"
    with open(groups_per_day_file_path, "r") as groups_per_day_file:
        groups_per_day = json.load(groups_per_day_file)
    group = groups_per_day[day_pointer[0]]
    return group
