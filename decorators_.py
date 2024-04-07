import random
import time

def timer_param(some_text: str):
    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time() + 1.2
            return f"{some_text} number {result} was generated in {end - start:.2f}"
        
        return wrapper
    return timer

@timer_param("FuncName")
def get_number(arg):
    return random.randint(1, 100) * arg

# result = timer(get_number)
# print(result(10))

# result = timer_param("Using get_number function")(get_number)(100)
# print(result)

print(get_number(10))