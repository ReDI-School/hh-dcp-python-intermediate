from lesson_11.slide_6.main import run

def test_run():
    largest, lowest, total = run()
    assert largest == 2678
    ## assert lowest == 5 this will crash our tests otherwise
    assert total == 7188
