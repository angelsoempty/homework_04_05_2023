def increase_result_by_100(func):
    def wrapper(numbers):
        result = func(numbers)
        return result + 100
    return wrapper

@increase_result_by_100
def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers_list = [1, 2, 3]
result = multiply_numbers(numbers_list)
print(f"Добуток чисел {numbers_list} збільшений на 100: {result}")
