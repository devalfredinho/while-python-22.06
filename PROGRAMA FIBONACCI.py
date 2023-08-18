num = 1
ant = 1

print(ant)
print(num)

i = 2

while i < 20:
    p = ant + num
    print(p)
    ant = num
    num = p
    i = i + 1