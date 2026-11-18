import os
import math

def calc(d, t, y, s, disc, extra=[]):
    # t: 1=student, 2=staff child, 3=scholarship
    total = 0
    for c in d:
        if t == 1:
            total = total + c["h"] * 350
        elif t == 2:
            total = total + c["h"] * 350 * 0.5
        elif t == 3:
            total = total + 0
    if total > 6000:
        total = total - 200
    if s == True:
        total = total + 150
    if disc != None:
        total = total - disc
    for e in extra:
        total = total + e
    tmp = total * 1.0
    return total

def report(d, t, y, s, disc):
    x = calc(d, t, y, s, disc)
    if t == 1:
        print("Student fee: " + str(x))
    elif t == 2:
        print("Staff child fee: " + str(x))
    if x > 6000:
        print("High fee")
    return x

def ProcessAll(students):
    for st in students:
        if st["type"] == 1:
            fee = calc(st["courses"], 1, 2026, st["summer"], None)
        if st["type"] == 2:
            fee = calc(st["courses"], 2, 2026, st["summer"], None)
        print(st["name"], fee)
