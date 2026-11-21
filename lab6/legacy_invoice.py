def make_invoice(student, kind):
    total = 0
    for code in student.courses:
        h = student.courses[code]
        if kind == "regular":
            total = total + h * 1200
        elif kind == "scholarship":
            total = total + h * 1200 * 0.5
        elif kind == "international":
            total = total + h * 2000
    if kind == "international":
        total = total + 5000
    text = "Invoice for " + student.student_id + ": " + str(int(total)) + " EGP"
    f = open("invoice_" + student.student_id + ".txt", "w")
    f.write(text)
    f.close()
    print(text)
    return total
