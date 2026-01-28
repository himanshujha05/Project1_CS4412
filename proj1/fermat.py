import random


def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):
    #Modular Exponentiation using recursive square-and-multiply algorithm
    #time complexity: O(log y)
    #space complexity: O(log y) due to recursion stack
    
    if y == 0: #base case x^0 = 1 for any x
    
        return 1
    
    # Here Recursive call: z = modexp(x, ⌊y/2⌋, N)
    # Compute x^(floor(y/2)) mod N
    z = mod_exp(x, y // 2, N)
    
    # here check if y is even or odd
    if y % 2 == 0:
        # if y is even then  return z^2 mod N
        return (z * z) % N
    else:
        # if y is odd then return x * z^2 mod N
        return (x * z * z) % N

def fprobability(k):
    # You will need to implement this function and change the return value.   
   #for composite numbers , atleast half of possible witness will detect compositeness 
    if k <= 0:# calculate probability of correcteness 
        return 0.0
    return 1.0 - (0.5 ** k)
   
#time complexity : O(1)
#space complexity : O(1)

def mprobability(k):
    # You will need to implement this function and change the return value.  
    # probability for the correctness for Miller-rfabin primality 
    if k <= 0:
        return 0.0
    return 1.0 - (0.25 ** k)
#time complexity : O(1)
#space complexity : O(1)

def fermat(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    #Here Fermat primality test , algorithm based on book 
    #if all k trail pass, N is a probable prime but could be a charmichael number 
    if N < 2:
        return 'composite'# number less than 2 are not prime 
    if N in (2, 3):
        return 'prime'#are smallest prime 
    if N % 2 == 0:
        return 'composite'# even numbers greater than 2 are not prime

   # Here run K indepoendent random trials 
    for _ in range(k):
        a = random.randint(2, N - 2)
        # Fermat check
        if mod_exp(a, N - 1, N) != 1:
            return 'composite'
# here it could be a charmichael number , false positive 
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

    # This decomposition is crucial for the square root sequenvce
    d = N - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Perform k trials
    # each trial has probability 1/4
    for _ in range(k):
        a = random.randint(2, N - 2)#chose random witness

        # Compute a^d mod N
        #taking square roots 
        x = mod_exp(a, d, N)

        # If x is 1 or -1 mod N, this round passes
        if x == 1 or x == N - 1:
            continue
        # try nopw next if above passed 
        # Square x up to s-1 times looking for -1 mod N
        found_minus_one = False
        for _ in range(s - 1):
            x = mod_exp(x, 2, N)
            if x == N - 1:
                found_minus_one = True
                break
            if x == 1:
                # Non-trivial square root of 1 => composite
                return 'composite'
    # here for the primes we must find  -1 before the sequence 
        if not found_minus_one:
            return 'composite'
  # All k trials passsed then N is probably prime.
    return 'prime'
    
