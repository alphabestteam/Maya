def calculate_factorial(chose_num):
    num_factional = 1
    for i in range(1, chose_num + 1):
        num_factional = num_factional * i
    return num_factional

def main():
    nums_sum = 0
    for i in range(101):
        nums_sum += i
    print(nums_sum)
    print(calculate_factorial(5))
    print(calculate_factorial(6))
    print(calculate_factorial(7))
    print(calculate_factorial(8))

if __name__ == "__main__":
    main()