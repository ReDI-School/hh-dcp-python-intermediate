# so make this work, you need to run the following command:
# pip install pytest


def fun(x):
    return x + 1

def test_fun():
    assert fun(3) == 4
