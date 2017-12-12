import sys


def sqrt(x):
    """
    Compute the square root using the method of Heron of Alexandria
    :param x:
    :return: ValueError on DivisionByZero
    """
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number {}".format(x))
    guess = x
    i = 0
    while guess * guess !=x and i < 20:
        guess =(guess + x/guess)/2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(11))
        print(sqrt(-1))
        print("This is never printed")
    except ValueError as e:
        print(e, file=sys.stderr)
    print("Program execution continues here")

if __name__ == '__main__':
    main()
