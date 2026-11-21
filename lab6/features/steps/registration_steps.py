from behave import given, then, when

from registration import RegistrationError, Student


@given('a student with ID "{sid}"')
def step_student(context, sid):
    context.student = Student(sid)
    context.error = None


@given("the student already has {n:d} registered hours")
def step_existing_hours(context, n):
    if n:
        context.student.register("FILLER", n)


@given('the student is registered for "{code}" worth {hours:d} hours')
def step_registered(context, code, hours):
    context.student.register(code, hours)


@when('the student registers for "{code}" worth {hours:d} hours')
def step_register(context, code, hours):
    try:
        context.student.register(code, hours)
    except RegistrationError as e:
        context.error = str(e)


@when('the student drops "{code}"')
def step_drop(context, code):
    try:
        context.student.drop(code)
    except RegistrationError as e:
        context.error = str(e)


@then("the student has {n:d} registered hours")
def step_hours(context, n):
    assert context.student.total_hours == n


@then('the registration is refused with "{text}"')
def step_refused(context, text):
    assert context.error is not None and text in context.error


@then('the result is "{result}"')
def step_result(context, result):
    actual = "refused" if context.error else "accepted"
    assert actual == result, actual
