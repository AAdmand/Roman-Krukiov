numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    for j in range(1, i - 1) :
        if i % j == 0 and j != 1:
            is_prime = False
            not_primes.append(i)
            break
        else :
            continue
    if is_prime and i != 1:
            primes.append(i)

print(primes, not_primes)


