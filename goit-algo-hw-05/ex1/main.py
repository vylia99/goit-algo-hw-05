def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n==1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610 
print(fib(1))  # Виведе 1
print(fib(0))  # Виведе 0  
print(fib(5))  # Виведе 5          
print(fib(25))  # Виведе 75025    