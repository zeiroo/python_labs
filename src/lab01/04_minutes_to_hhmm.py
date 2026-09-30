minutes = int(input("Минуты: "))
hours = minutes // 60

print(f'{hours}:{(minutes % 60):02d}')