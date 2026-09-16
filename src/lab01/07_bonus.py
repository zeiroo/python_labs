inp = str(input())
out = ""
step = 0
start = 0

for i in range(len(inp)):
    char = inp[i]
    if char == char.upper():
        out += char
        start = i
        break

for i in range(start, len(inp)):
    char = inp[i]
    if char.isdigit():
        step = i + 1 - start
        break

for i in range(start + step, len(inp), step):
    char = inp[i]
    out += char

print(out)
    