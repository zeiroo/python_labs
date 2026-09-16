fio = (str(input())).split()
surname, name, father = fio[0], fio[1], fio[2]
initials = surname[0] + name[0] + father[0]
length = len(surname+name+father) + 2

print(f'Инициалы: {initials}.\nДлина (символов): {length}')
