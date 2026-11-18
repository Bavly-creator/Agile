"""Turn a score from 0 to 100 into a letter grade."""

MIN_SCORE = 0
MAX_SCORE = 100
GRADE_THRESHOLDS = (
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
)
FAIL_GRADE = "F"


def letter_grade(score):
    """Return the letter for a score; raise ValueError outside 0-100."""
    if not MIN_SCORE <= score <= MAX_SCORE:
        raise ValueError(f"score must be between {MIN_SCORE} and {MAX_SCORE}")
    for minimum, letter in GRADE_THRESHOLDS:
        if score >= minimum:
            return letter
    return FAIL_GRADE