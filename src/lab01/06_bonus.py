num = int(input("in_1: "))

ochn = 0
neochn = 0
counter = 1
for _ in range(num):
    counter += 1
    info = str(input(f"in_{counter}: ")).split()
    surname, name, age, form = info[0], info[1], info[2], info[3]

    if form == "True":
        ochn += 1
    elif form == "False":
        neochn += 1

print("out:", ochn, neochn)