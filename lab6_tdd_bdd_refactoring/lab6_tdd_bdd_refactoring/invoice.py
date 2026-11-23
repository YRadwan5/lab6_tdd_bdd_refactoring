FEE_PER_HOUR = 1200
INTERNATIONAL_RATE = 2000
INTERNATIONAL_SERVICE_FEE = 5000
SCHOLARSHIP_DISCOUNT = 0.50
SIBLING_DISCOUNT = 0.25


class RegularPolicy:
    def fee(self, hours):
        return hours * FEE_PER_HOUR


class ScholarshipPolicy:
    def fee(self, hours):
        return hours * FEE_PER_HOUR * SCHOLARSHIP_DISCOUNT


class InternationalPolicy:
    def fee(self, hours):
        return hours * INTERNATIONAL_RATE + INTERNATIONAL_SERVICE_FEE


class SiblingPolicy:
    """Sibling students receive a 25% discount on the regular fee."""

    def fee(self, hours):
        return hours * FEE_PER_HOUR * (1 - SIBLING_DISCOUNT)


POLICIES = {
    "regular": RegularPolicy(),
    "scholarship": ScholarshipPolicy(),
    "international": InternationalPolicy(),
    "sibling": SiblingPolicy(),
}


class FileWriter:
    def write(self, student_id, text):
        with open(f"invoice_{student_id}.txt", "w", encoding="utf-8") as file:
            file.write(text)


def make_invoice(student, kind, writer=None):
    """Calculate an invoice and delegate persistence to an injected writer."""
    try:
        policy = POLICIES[kind]
    except KeyError as exc:
        raise ValueError(f"Unknown student kind: {kind}") from exc

    total = policy.fee(student.total_hours)
    invoice_text = f"Invoice for {student.student_id}: {int(total)} EGP"
    (writer or FileWriter()).write(student.student_id, invoice_text)
    return total
