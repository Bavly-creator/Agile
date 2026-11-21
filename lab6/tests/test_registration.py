import pytest

from registration import RegistrationError, Student


def test_register_adds_hours():
    s = Student("2023001")
    s.register("SET312", 3)
    assert s.total_hours == 3
