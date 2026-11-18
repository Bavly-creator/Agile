import pytest
from fees import Course, StudentType, fee_report, process_all, tuition_fee
from legacy_fees import calc


def legacy_courses(*hours):
    return [{"h": h} for h in hours]


def courses(*hours):
    return [Course(h) for h in hours]


def student(name, kind):
    return {"name": name, "type": kind, "courses": courses(3), "summer": False}


@pytest.mark.parametrize(
    "hours, code, kind, summer",
    [
        ((3, 3, 3), 1, StudentType.REGULAR, False),
        ((3, 3, 3, 3, 3, 3), 1, StudentType.REGULAR, True),
        ((3, 4), 2, StudentType.STAFF_CHILD, False),
        ((3, 3), 3, StudentType.SCHOLARSHIP, True),
    ],
)
def test_same_result_as_legacy(hours, code, kind, summer):
    old = calc(legacy_courses(*hours), code, 2026, summer, None)
    new = tuition_fee(courses(*hours), kind, summer)
    assert new == old


def test_large_fee_gets_reduction():
    # 18 hours x 350 = 6300 > 6000, so 200 is taken off
    assert tuition_fee(courses(6, 6, 6), StudentType.REGULAR) == 6100


def test_scholarship_student_is_not_skipped():
    students = [
        student("Sara", StudentType.REGULAR),
        student("Omar", StudentType.SCHOLARSHIP),
    ]
    assert process_all(students) == {"Sara": 1050, "Omar": 0}


def test_scholarship_first_in_list_does_not_crash():
    assert process_all([student("Omar", StudentType.SCHOLARSHIP)]) == {"Omar": 0}


def test_discount_is_subtracted():
    assert tuition_fee(courses(3), StudentType.REGULAR, discount=50) == 1000


def test_extras_are_added():
    assert tuition_fee(courses(3), StudentType.REGULAR, extras=(10, 20)) == 1080


def test_report_is_text_and_marks_high_fee():
    text = fee_report(courses(6, 6, 6), StudentType.REGULAR)
    assert text == "Student fee: 6100\nHigh fee"
