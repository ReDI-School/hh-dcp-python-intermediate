from lesson_11.exercise_2.main import increase

def test_increase():
    assert increase("13,27,5,67,39,2,10,89,41,7,9,73") == "15,29,7,69,41,4,12,91,43,9,11,75"


def test_empty():
    assert increase("") == ""
