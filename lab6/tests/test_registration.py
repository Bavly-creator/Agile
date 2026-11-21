import pytest

from registration import RegistrationError, Student


def test_register_adds_hours():
    s = Student("2023001")
    s.register("SET312", 3)
    assert s.total_hours == 3


def test_cannot_go_over_18_hours():
    s = Student("2023001")
    s.register("SET312", 15)
    with pytest.raises(RegistrationError):
        s.register("SET472", 4)
    assert s.total_hours == 15


def test_cannot_register_same_course_twice():
    s = Student("2023001")
    s.register("SET312", 3)
    with pytest.raises(RegistrationError):
        s.register("SET312", 3)


def test_drop_removes_course():
    s = Student("2023001")
    s.register("SET312", 3)
    s.drop("SET312")
    assert s.total_hours == 0
