


def main():
    num_get = int(input('how many fibonacci numbers do you wanna see?: '))
    fibonacci_generator(num_get)

def fibonacci_generator(numbers):
    fibo = [0, 1]
    index = 0
    for count in range(numbers):
        print(f' Number [{index}]: {fibo[index]}')
        index += 1
        if index >= 2:
            newfibo = fibo[index - 1] + fibo[index - 2]
            fibo.append(newfibo)


if __name__ == '__main__':
    main()


