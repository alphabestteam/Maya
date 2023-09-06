def calculate_factorial(chose_num):
    num_factional = 1
    for i in range(1, chose_num + 1):
        num_factional = num_factional * i
    return num_factional

def prime_nums(input_num):
    """
    function that gets a number and returns all the prime numbers until that number including the number
    """
    prime_nums_list = []
    for i in range(2, input_num + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag == True:
            prime_nums_list.append(i)
    return prime_nums_list
                    

def main():
    nums_sum = 0
    for i in range(101):
        nums_sum += i
    print(nums_sum)
    print(calculate_factorial(5))
    print(calculate_factorial(6))
    print(calculate_factorial(7))
    print(calculate_factorial(8))
    print(prime_nums(5))
    print(prime_nums(6))
    print(prime_nums(7))
    print(prime_nums(14))
    print(prime_nums(152))
    print(prime_nums(60693))

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