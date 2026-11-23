import pytest

from invoice import make_invoice
from registration import Student


@pytest.fixture
def student():
    student = Student("2023001")
    student.register("SET312", 3)
    student.register("SET472", 3)
    return student


@pytest.mark.parametrize(
    ("kind", "expected"),
    [
        ("regular", 7200),
        ("scholarship", 3600),
        ("international", 17000),
    ],
)
def test_invoice_totals_preserve_legacy_behaviour(
    student, kind, expected, tmp_path, monkeypatch
):
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


def test_sibling_policy_gives_25_percent_discount(student):
    fake = FakeWriter()
    total = make_invoice(student, "sibling", writer=fake)
    assert total == 5400
    assert fake.saved["2023001"] == "Invoice for 2023001: 5400 EGP"


def test_unknown_student_kind_has_clear_error(student):
    with pytest.raises(ValueError, match="Unknown student kind"):
        make_invoice(student, "unknown", writer=FakeWriter())
