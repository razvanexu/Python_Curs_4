lungimea = input("Introduceti lungimea: ")
latimea = input("introduceti latimea: ")


def aria(lungimea, latimea=0):
    if latimea == "" or latimea == "0":
        latimea = lungimea

    return int(lungimea) * int(latimea)


print(aria(lungimea, latimea))
