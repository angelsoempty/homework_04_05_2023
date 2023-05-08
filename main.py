import time

def limit_rate(max_calls, time_period):
    def decorator(func):
        call_times = []
        def wrapper(*args, **kwargs):
            current_time = time.time()
            call_times[:] = [t for t in call_times if t >= current_time - time_period]
            if len(call_times) < max_calls:
                call_times.append(current_time)
                return func(*args, **kwargs)
            else:
                print(f"Ліміт кількості викликів ({max_calls}) за проміжок часу ({time_period} секунд) вичерпано.")
        return wrapper
    return decorator

@limit_rate(max_calls=3, time_period=10)
def my_function():
    print("Ця функція може бути викликана не більше 3 разів протягом 10 секунд.")

my_function()
time.sleep(2)
my_function()
my_function()
my_function()
