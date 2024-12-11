limit = 10000
sieve = [True] * (limit + 1)
sieve[0] = sieve[1] = False  # 0 and 1 are not prime

for i in range(2, int(limit ** 0.5) + 1):
    if sieve[i]:
        for multiple in range(i * i, limit + 1, i):  # Mark multiples of i
            sieve[multiple] = False

primes = [i for i, is_prime in enumerate(sieve) if is_prime]
print(primes)