import random

def nums_sum(first_num = 0, second_num = 0) -> int:
    """
    Q5
    a function that returns the sum of two numbers
    """
    return first_num + second_num

def print_message(name: str) -> None:
    """
    Q6
    a function that greets a person
    """
    print(f"Hello {name}! Great to see u")

def quadratic_eq_solution(a, b, c):
    """
    function gets numbers: a, b, c from user and returns the solutions of a quadratic equations with 
    the numbers if possible.
    """
    inside_root = (b**2) - (4*a*c)
    if inside_root < 0:
        return "This equation cannot be solved!"
    else:    
        solution1 = (-b-inside_root**0.5) / (2*a)
        solution2 = (-b+inside_root**0.5) / (2*a)
        return solution1, solution2

def random_int(first_number: int, second_number: int) -> int:
    return random.randint(first_number, second_number)

def random_double(first_number: float, second_number: float) -> float:
    return random.uniform(first_number, second_number)