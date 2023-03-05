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

