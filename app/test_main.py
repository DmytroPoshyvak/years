from app import main


def test_should_return_zero_for_0_years() -> None:
    assert main.get_human_age(0, 0) == [0, 0]


def test_should_return_zero_before_15_years() -> None:
    assert main.get_human_age(14, 14) == [0, 0]


def test_should_return_one_at_15_years() -> None:
    assert main.get_human_age(15, 15) == [1, 1]


def test_should_return_one_before_24_years() -> None:
    assert main.get_human_age(23, 23) == [1, 1]


def test_should_return_two_at_24_years() -> None:
    assert main.get_human_age(24, 24) == [2, 2]


def test_should_return_two_at_27_years() -> None:
    assert main.get_human_age(27, 27) == [2, 2]


def test_should_return_three_cat_and_two_dog_at_28_years() -> None:
    assert main.get_human_age(28, 28) == [3, 2]


def test_should_return_21_cat_and_17_dog_at_100_years() -> None:
    assert main.get_human_age(100, 100) == [21, 17]