# Sieve of Eratosthenes - print primes.
N = 10000
is_prime = [True] * N
for i in range(2, int(N ** 0.5)):
    if is_prime[i]:
        for j in range(i * i, N, i):
            is_prime[j] = False
p = 0
for i in range(2, N):
    if is_prime[i]:
        print(i, end = ' ')
        p += 1
        if p % 10 == 0:
            print() # New line.
print("\nTotal of", p, "primes")
