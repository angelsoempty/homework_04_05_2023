import time
def timeit_decorator(func):
    def wrapper(number):
        start_time = time.time()
        result = func(number)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання функції: {execution_time} секунд")
        return result
    return wrapper
@timeit_decorator
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

num = 37
is_prime_num = is_prime(num)
if is_prime_num:
    print(f"Число {num} є простим")
else:
    print(f"Число {num} не є простим")
