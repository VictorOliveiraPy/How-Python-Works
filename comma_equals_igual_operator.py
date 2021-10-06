# variavel , = variavel = troca os valores


def do_something():
    primes = {2, 3, 5, 7, 11}
    evens = {2, 4, 6, 8, 10}

    x, = primes.intersection(evens)
    print(x)


if __name__ == '__main__':
    do_something()
    x = 1
    a = [2]

    y = [9]

    x, = a

