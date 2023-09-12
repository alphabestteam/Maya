def words_length(*args):
    words_len = []
    for index in range(len(args)):
        words_len.append(len(args[index]))
    return words_len

def total_age(**kwargs):
    print(kwargs)
    sum_values = 0
    for key in kwargs:
        sum_values += kwargs[key]
    return sum_values

def main():
    print(words_length("msmms", "blahblah", "helow"))
    print(total_age(age1= 20, age2 = 31, age3 = 19, age4 = 42))
if __name__ == "__main__":
    main()