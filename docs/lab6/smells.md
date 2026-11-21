

\# Task C1 — Code smells in legacy\_invoice.py (found before changing anything)



| Smell | Where | Principle it breaks |

|---|---|---|

| Long if/elif chain on `kind` (checked twice) | loop body + after the loop | OCP: a new student type means editing this function |

| Magic numbers 1200, 0.5, 2000, 5000 | inside the chain | Readability: the meaning of each number is hidden |

| One function calculates the fee, formats the text, writes a file and prints | the whole function | SRP: four reasons to change |

| File opened without `with` and closed by hand | `open(...)` / `f.close()` | Resource safety: file stays open if `write` fails |

| Disk and `print` hard-wired inside the function | last lines | DIP: cannot be tested without writing files |

| Fee worked out per course although only the total hours matter | the `for` loop | Needless complexity |

| Unknown `kind` silently gives 0 EGP and still writes an invoice | no `else` branch | Hidden bug: no validation |



