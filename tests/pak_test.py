from pakname import Shrubbery, additional


def test_shrub():
    s = Shrubbery(10, 10)
    s.describe()


def test_additional():
    assert additional() == 0.
