"""Tuition fee calculation for the Student Services App."""

from dataclasses import dataclass
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


RATE_SHARE = {
    StudentType.REGULAR: 1,
    StudentType.STAFF_CHILD: 0.5,
    StudentType.SCHOLARSHIP: 0,
}

TYPE_LABELS = {
    StudentType.REGULAR: "Student fee",
    StudentType.STAFF_CHILD: "Staff child fee",
}


@dataclass(frozen=True)
class Course:
    """A course the student registered for."""

    hours: int


def tuition_fee(courses, student_type, summer=False, discount=0, extras=()):
    """Calculate the tuition fee for one student."""
    total = sum(course.hours for course in courses) * RATE_PER_HOUR
    total *= RATE_SHARE[student_type]

    if total > HIGH_FEE_LIMIT:
        total -= HIGH_FEE_REDUCTION
    if summer:
        total += SUMMER_SURCHARGE
    total -= discount

    return total + sum(extras)


def fee_report(courses, student_type, summer=False, discount=0):
    """Return a text report for one student."""
    fee = tuition_fee(courses, student_type, summer, discount)
    lines = []

    if student_type in TYPE_LABELS:
        lines.append(f"{TYPE_LABELS[student_type]}: {fee}")
    if fee > HIGH_FEE_LIMIT:
        lines.append("High fee")

    return "\n".join(lines)


def process_all(students):
    """Process regular and staff-child students."""
    for student in students:
        if student["type"] == StudentType.REGULAR:
            fee = tuition_fee(
                student["courses"], StudentType.REGULAR, student["summer"]
            )
        if student["type"] == StudentType.STAFF_CHILD:
            fee = tuition_fee(
                student["courses"], StudentType.STAFF_CHILD, student["summer"]
            )
        print(student["name"], fee)