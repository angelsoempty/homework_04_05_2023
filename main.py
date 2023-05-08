def log_decorator(func):
    def wrapper(celsius):
        result = func(celsius)
        print(f"Перетворення температури: {celsius}C -> {result}F")
        return result
    return wrapper

@log_decorator
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
temperature_celsius = 25
temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
print(f"Температура {temperature_celsius}C дорівнює {temperature_fahrenheit}F")
