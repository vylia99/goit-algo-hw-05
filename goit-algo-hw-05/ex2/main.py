from typing import Callable
import re
def generator_numbers(text: str):
    numbers = re.findall(r'\b\d+\.\d+|\b\d+\b', text) # Пошук всіх дійсних чисел
    for num in numbers:
        yield float(num)  # Повертаємо кожне число як генератор

def sum_profit(text: str, func: Callable):
    return sum(func(text)) # Використовуємо генератор для підсумовування чисел
    
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
