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


class FakeWriter:
    def __init__(self):
        self.saved = {}

    def write(self, student_id, text):
        self.saved[student_id] = text


def test_invoice_uses_injected_writer(student):
    fake = FakeWriter()
    make_invoice(student, "regular", writer=fake)
    assert fake.saved["2023001"] == "Invoice for 2023001: 7200 EGP"


def test_sibling_discount_is_25_percent_off_regular(student):
    fake = FakeWriter()
    total = make_invoice(student, "sibling", writer=fake)
    assert total == 5400
    assert fake.saved["2023001"] == "Invoice for 2023001: 5400 EGP"
