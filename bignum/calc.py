print('computing initial')
power = 2**100000000
for num in range(100000000,1000000000):
    print(num, end='\r', flush=True)
    power *= 2
    if power % 100000000 == num:
        print('SOLUTION!!',num)

