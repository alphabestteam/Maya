import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(9, 4)
        end_time = time.time()
        return end_time - start_time
    return wrapper

@timer
def test_func(a, b):
    c = a + b
    return c / 100

def return_sequence(N: int) -> int:
    index_before = 2
    index_two_before = 1
    for index in range(1, N + 1):
        if index == 1:
            yield 1
        elif index == 2:
            yield 2
        else: 
            new_value = index_before * index_two_before
            yield new_value
            index_two_before = index_before
            index_before = new_value

def main():
    print(test_func())

    for value in return_sequence(5):
        print(value)

        
if __name__ == "__main__":
    main()