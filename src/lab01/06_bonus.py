num = int(input())

ochn = 0
neochn = 0

for _ in range(num):
    info = str(input()).split()
    surname, name, age, form = info[0], info[1], info[2], info[3]

    if form == "True":
        ochn += 1
    elif form == "False":
        neochn += 1

print(ochn, neochn)