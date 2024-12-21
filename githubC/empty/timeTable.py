a = 2  
for b in range(9):
    print('a x b =' a*b)
    a++

a = 2
b = 0
while a <= 9:
    b += 1
    print(f'{a} x {b} = {a*b}')
    if b == 9:
        a += 1
        b = 0
