name_1 = input("Unesite svoje ime: ")
name_2 = input("Unesite ime protivnika: ")
wins = int(input("Do koliko se igra: "))
score_1 = 0
score_2 = 0


def rock_scissors():
    if first == second:
        return 3
    if \
            (first == "kamen" and second == "makaze") or \
            (first == "makaze" and second == "papir") or \
            (first == "papir" and second == "kamen"):
        return 1
    return 2


while (score_1 < wins and score_2 < wins) or abs(score_1 - score_2) < 2:
    first = input("Papir, kamen, makaze? ")
    while first not in ("kamen", "papir", "makaze"):
        first = input("Papir, kamen, makaze? ")
    second = input("Papir, kamen, makaze? ")
    while second not in ("kamen", "papir", "makaze"):
        second = input("Papir, kamen, makaze? ")
    score = rock_scissors()
    if score == 3:
        pass
    elif score == 1:
        score_1 += 1
    elif score == 2:
        score_2 += 1
    print(score_1)
    print(score_2)
print()
