import timeit


def while_loop(n=100_000_000):
    i = 0
    s = 0

    while i < n:
        s += i
        i += 1
    return s


# A parte de interacao do for e escrita em C
def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += 1
    return s


def sum_range(n=100_000_000):
    return sum(range(n))


def main():
    print('while loop\t\t', timeit.timeit(while_loop, number=1))
    print('for pure\t\t', timeit.timeit(for_loop, number=1))
    print('sum range\t\t', timeit.timeit(sum_range, number=1))


if __name__ == '__main__':
    main()
