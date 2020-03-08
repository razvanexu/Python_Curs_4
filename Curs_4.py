r = [1.2, 3.5, -1.9, -2.8, 0.9]
r = list(map(lambda x: int(x), r))

print(r)


poz = list(filter(lambda x: x>=0, r))

print(poz)

str = "O chicat o perja-n glod"
res = str.split(" ", 2)

print(res)