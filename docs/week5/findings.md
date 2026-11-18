# Week 5 — Findings: static analysis of `legacy_fees.py`

**Team 7 — FocusPulse** · Tools: Ruff 0.16.9 (rules E, F, B, N, SIM, C90, PLR, ARG, max-complexity 5) and Pylint 4.1.4. Full output is in `before.txt`.

Ruff reports **17 problems** (the handout says 16; our newer Ruff version also reports `PLR0917` too-many-positional-arguments on the same line as `PLR0913`). Pylint rates the file **4.86 / 10**.

## 1. Findings table

| Rule | Count | Smell (lecture name) | Refactoring that removes it |
|------|:-----:|----------------------|-----------------------------|
| F401 | 2 | Dead code (unused imports `os`, `math`) | Delete the imports |
| PLR2004 | 6 | Magic numbers (`2`, `3`, `6000` in comparisons) | Replace with named constants / an Enum |
| C901 | 1 | Long method with many branches (complexity 9 > 5) | Replace the if/elif chain with a rate table; extract small steps |
| PLR0913 / PLR0917 | 1 + 1 | Long parameter list (6 arguments) | Remove the unused argument `y`; give the arguments defaults; group data in a class |
| ARG001 | 1 | Dead code (unused argument `y`) | Delete the argument |
| B006 | 1 | Mutable default argument (`extra=[]` is shared between calls) | Use an immutable default `extras=()` |
| E711 / E712 | 1 + 1 | Wrong comparison style (`!= None`, `== True`) | `if summer:` and a default of `0` for the discount |
| F841 | 1 | Dead code (unused variable `tmp`) | Delete the variable |
| N802 | 1 | Mysterious / badly named function (`ProcessAll`) | Rename to `process_all` (and `calc` to `tuition_fee`) |

Pylint's own warnings point to the same smells: `unused-import`, `dangerous-default-value`, `singleton-comparison`, `invalid-name`, `unused-argument`, `unused-variable`, `too-many-arguments`, and missing docstrings (`missing-function-docstring`).

## 2. Extra smells that Ruff did not report

1. **Mysterious names** — `d`, `t`, `y`, `s`, `c`, `e`, `x`, `st`, `disc`. A reader cannot tell what `t == 2` or `s` means without the comment. Rename to `courses`, `student_type`, `summer`, `discount`.
2. **Magic numbers in calculations** — `350`, `0.5`, `200` and `150` are used inside the arithmetic (Ruff only flags numbers in comparisons). Replace with named constants such as `RATE_PER_HOUR` and `SUMMER_SURCHARGE`.
3. **Duplicated code / mixed responsibilities** — `report()` calculates and prints in the same function, and `ProcessAll` repeats the same `calc(...)` call for each type. The calculation should return a value, and printing should be separate.
4. **Primitive obsession / type codes** — the student type is the number 1, 2 or 3 (explained only in a comment), and a course is a dictionary `{"h": ...}`. Use an Enum and a small `Course` class.
5. **Pointless statement** — `total = total + 0` for scholarship students does nothing, and `ProcessAll` uses two separate `if` blocks instead of one decision.

## 3. The hidden bug in `ProcessAll`

Running `ProcessAll` with Sara (type 1) and Omar (type 3) prints `Sara 1050` and `Omar 1050`. Omar is a scholarship student who should pay 0, but `ProcessAll` only sets `fee` for types 1 and 2, so for type 3 no `if` runs and `fee` still holds Sara's value from the previous loop turn, and Omar is charged her fee. If Omar is the first student in the list, `fee` has never been set and Python raises `UnboundLocalError`. Pylint hints at this with `possibly-used-before-assignment` (E0606) on the `print` line. The fix is to calculate a fee for every student, including type 3 (fee 0).
