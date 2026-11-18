"""Tuition fee calculation for the Student Services App."""

from enum import Enum

RATE_PER_HOUR = 350
HIGH_FEE_LIMIT = 6000
HIGH_FEE_REDUCTION = 200
SUMMER_SURCHARGE = 150


class StudentType(Enum):
    """The kinds of students."""

    REGULAR = 1
    STAFF_CHILD = 2
    SCHOLARSHIP = 3


def tuition_fee(courses, student_type, summer, discount, extra=[]):
    """Calculate the tuition fee for one student."""
    total = 0

    for course in courses:
        if student_type == StudentType.REGULAR:
            total += course["h"] * RATE_PER_HOUR
        elif student_type == StudentType.STAFF_CHILD:
            total += course["h"] * RATE_PER_HOUR * 0.5
        elif student_type == StudentType.SCHOLARSHIP:
            total += 0

    if total > HIGH_FEE_LIMIT:
        total -= HIGH_FEE_REDUCTION
    if summer == True:
        total += SUMMER_SURCHARGE
    if discount != None:
        total -= discount

    for extra_fee in extra:
        total += extra_fee

    return total


def report(courses, student_type, summer, discount):
    """Print a fee report."""
    fee = tuition_fee(courses, student_type, summer, discount)
    if student_type == StudentType.REGULAR:
        print("Student fee: " + str(fee))
    elif student_type == StudentType.STAFF_CHILD:
        print("Staff child fee: " + str(fee))
    if fee > HIGH_FEE_LIMIT:
        print("High fee")
    return fee


def process_all(students):
    """Process regular and staff-child students."""
    for student in students:
        if student["type"] == StudentType.REGULAR:
            fee = tuition_fee(student["courses"], StudentType.REGULAR,
                              student["summer"], None)
        if student["type"] == StudentType.STAFF_CHILD:
            fee = tuition_fee(student["courses"], StudentType.STAFF_CHILD,
                              student["summer"], None)
        print(student["name"], fee)