def is_prime(n):
    sez = []
    for i in range(1, int(n + 1)):
        if n % i == 0:
            sez += [i]
    return len(sez) == 2


for i in range(1, 201):
    if is_prime(i):
        print(i)

      