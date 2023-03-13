import random

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        #print(f"Function {func.__name__} has been called {wrapper.count} times.")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@count_calls
def is_equal(x, y): return x==y

@count_calls
def is_not_equal(x, y): return x!=y



def fibonacci_word(n):
    if n == 0:
        return ""
    if n == 1:
        return "0"
    if n == 2:
        return "01"
    prev_prev = "0"
    prev = "01"
    fib_word = ""
    for i in range(3, n+1):
        fib_word = prev + prev_prev
        prev_prev = prev
        prev = fib_word
    return fib_word





def is_prime(n, k=5):
    """
    Miller-Rabin primality test. Returns True if n is probably prime, False otherwise.
    k is the number of iterations to perform. Higher values of k increase the accuracy of the test.
    """
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    
    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

def random_prime(n_bits):
    """
    Generates a large prime number with n_bits bits.
    """
    while True:
        p = random.getrandbits(n_bits)
        if is_prime(p):
            return p
