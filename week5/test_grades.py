import pytest
from grades import letter_grade


def test_ninety_is_an_a():
    assert letter_grade(90) == "A"


def test_eighty_nine_is_a_b():
    assert letter_grade(89) == "B"


def test_below_sixty_fails():
    assert letter_grade(59) == "F"


def test_score_above_100_is_rejected():
    with pytest.raises(ValueError):
        letter_grade(101)


def test_zero_is_an_f():
    assert letter_grade(0) == "F"


def test_one_hundred_is_an_a():
    assert letter_grade(100) == "A"


def test_sixty_is_a_d():
    assert letter_grade(60) == "D"


def test_sixty_nine_is_a_d():
    assert letter_grade(69) == "D"


def test_seventy_is_a_c():
    assert letter_grade(70) == "C"


def test_negative_score_is_rejected():
    with pytest.raises(ValueError):
        letter_grade(-1)
