FEE_PER_HOUR = 1200


class RegularPolicy:
    def fee(self, hours):
        return hours * FEE_PER_HOUR


class ScholarshipPolicy:
    def fee(self, hours):
        return hours * FEE_PER_HOUR * 0.5


class SiblingPolicy:
    DISCOUNT = 0.25

    def fee(self, hours):
        return hours * FEE_PER_HOUR * (1 - self.DISCOUNT)


class InternationalPolicy:
    RATE = 2000
    SERVICE_FEE = 5000

    def fee(self, hours):
        return hours * self.RATE + self.SERVICE_FEE


POLICIES = {
    "regular": RegularPolicy(),
    "scholarship": ScholarshipPolicy(),
    "international": InternationalPolicy(),
    "sibling": SiblingPolicy(),
}


class FileWriter:
    def write(self, student_id, text):
        with open(f"invoice_{student_id}.txt", "w") as f:
            f.write(text)


def make_invoice(student, kind, writer=None):
    policy = POLICIES[kind]
    total = policy.fee(student.total_hours)
    text = f"Invoice for {student.student_id}: {int(total)} EGP"
    (writer or FileWriter()).write(student.student_id, text)
    return total
