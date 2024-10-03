#!/usr/bin/python3
""""""
def isWinner(x, nums):
    if not nums or x <= 0:
        return None

    # Find the maximum number in nums to limit the sieve of Eratosthenes
    max_n = max(nums)
    
    # Sieve of Eratosthenes to find all primes up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Precompute number of primes up to each n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Maria and Ben's win counts
    maria_wins = 0
    ben_wins = 0

    # Process each game round
    for n in nums:
        # If the number of primes up to n is odd, Maria wins, otherwise Ben wins
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None