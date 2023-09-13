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

def main():
    print(test_func())

if __name__ == "__main__":
    main()