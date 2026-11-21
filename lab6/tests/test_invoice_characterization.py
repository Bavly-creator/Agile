import pytest

from invoice import make_invoice
from registration import Student


@pytest.fixture
def student():
    s = Student("2023001")
    s.register("SET312", 3)
    s.register("SET472", 3)
    return s


@pytest.mark.parametrize("kind, expected", [
    ("regular", 7200),
    ("scholarship", 3600),
    ("international", 17000),
])
def test_invoice_total(student, kind, expected, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert make_invoice(student, kind) == expected
