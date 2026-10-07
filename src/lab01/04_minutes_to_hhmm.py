minutes = int(input("Минуты: "))
hours = minutes // 60

print(f'{hours%24}:{(minutes % 60):02d}')