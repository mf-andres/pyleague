from pyleague.main import generate_groups_per_day


def test_generate_groups_per_day_works_correctly_for_even_participants():
    participants = ["a", "b", "c", "d"]
    groups_per_day = generate_groups_per_day(participants)
    expected_groups_per_day = [
        ['a', 'b', 'c', 'd'],
        ['a', 'd', 'b', 'c'],
        ['a', 'c', 'd', 'b'],
    ]
    assert groups_per_day == expected_groups_per_day
