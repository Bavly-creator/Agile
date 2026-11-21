FEE_PER_HOUR = 1200


class RegularPolicy:
    def fee(self, hours):
        return hours * FEE_PER_HOUR


class ScholarshipPolicy:
    def fee(self, hours):
        return hours * FEE_PER_HOUR * 0.5


class InternationalPolicy:
    RATE = 2000
    SERVICE_FEE = 5000

    def fee(self, hours):
        return hours * self.RATE + self.SERVICE_FEE


def make_invoice(student, kind):
    if kind == "regular":
        policy = RegularPolicy()
    elif kind == "scholarship":
        policy = ScholarshipPolicy()
    else:
        policy = InternationalPolicy()
    total = policy.fee(student.total_hours)
    text = "Invoice for " + student.student_id + ": " + str(int(total)) + " EGP"
    f = open("invoice_" + student.student_id + ".txt", "w")
    f.write(text)
    f.close()
    print(text)
    return total
