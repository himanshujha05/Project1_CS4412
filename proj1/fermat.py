import random


def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):
    

    result = 1
    base = x % N      # reduce x modulo N first
    exp = y

    while exp > 0:
        # If exp is odd, multiply result by current base
        if exp % 2 == 1:
            result = (result * base) % N

        # Square the base
        base = (base * base) % N

        # Divide exponent by 2
        exp = exp // 2

    return result

def fprobability(k):
    # You will need to implement this function and change the return value.   
    if k <= 0:
        return 0.0
    return 1.0 - (0.5 ** k)
   


def mprobability(k):
    # You will need to implement this function and change the return value.   
    if k <= 0:
        return 0.0
    return 1.0 - (0.25 ** k)


def fermat(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    if N < 2:
        return 'composite'
    if N in (2, 3):
        return 'prime'
    if N % 2 == 0:
        return 'composite'

    # Run k random Fermat trials
    # Pick random a in [2, N-2]
    for _ in range(k):
        a = random.randint(2, N - 2)
        # Fermat check: a^(N-1) ≡ 1 (mod N) for prime N
        if mod_exp(a, N - 1, N) != 1:
            return 'composite'

    return 'prime'
   


def miller_rabin(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    if N < 2:
        return 'composite'
    if N in (2, 3):
        return 'prime'
    if N % 2 == 0:
        return 'composite'

    # Write N-1 as 2^s * d where d is odd
    d = N - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Perform k trials
    for _ in range(k):
        a = random.randint(2, N - 2)

        # Compute a^d mod N
        x = mod_exp(a, d, N)

        # If x is 1 or -1 mod N, this round passes
        if x == 1 or x == N - 1:
            continue

        # Square x up to s-1 times looking for -1 mod N
        found_minus_one = False
        for _ in range(s - 1):
            x = (x * x) % N
            if x == N - 1:
                found_minus_one = True
                break
            if x == 1:
                # Non-trivial square root of 1 => composite
                return 'composite'

        if not found_minus_one:
            return 'composite'

    return 'prime'
    
