from app.operations import addition


def test_addition():
    a = 1
    b = 2

    c = addition(a,b)

    assert c == 3