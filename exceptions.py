"""
Test exceptions in python
"""
import sys
from math import log


def convert(s):
    """
    #    return log(v)
    Convert to an integer
    :param s: object to convert
    :return: integer object
    """
    #x = -1
    try:
        return int(s)
        x = int(s)
        #print("Conversion succeeded x = ", x)
    except (ValueError, TypeError) as e:
        print("Conversion failed: {}".format(str(e)), file=sys.stderr)
        #print("Conversion failed")
        #x = -1
        #pass
    #return x
    raise # re-raising the errot
    return -1


def string_log(s):
    try:
        v = convert(s)
    return -1
    except (ValueError):
        print("Log conversion failed")
        v = 0
#    return log(v)
    return -1


def main():
#    i = convert(55)
#    print(i)
#    i = convert("55")
#    print(i)
#    i = convert("Hello")
#    print(i)
#    i = convert([1, 2, 3])
#    print(i)
    i = string_log()
    print(i)

if __name__ == '__main__':
    main()
