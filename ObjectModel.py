"""
Ojbect Model test scripts
"""


def modify(k):
    """
    Modifies the content of my list
    :param k:
    :return:
    """
    k.append(33)
    print("k= ", k)

def replace(g):
    """
    Replace the content of the list
    :param g: list object
    :return: nothing
    """
    g = [17, 36, 22, 33]
    print("g = ", g)

def update_info(g):
    """
    Updates list content byh incrementing each memeber by 1
    :param g:
    :return:
    """
#    c = 0
#    for i in g:
#        i += 1
#        g[c] = i
#        c += 1
    i = 0
    while i < len(g):
        g[i] += 1
        i += 1
    print("g = ", g)

def banner(message, border = '*'):
    """
    Displays message surrounded by border
    :param message: message string
    :param border: border style (char). Optional with a default value of '*'
    :return: nothing
    """
    line = border*(len(message)+4)
    print(line)
    print(border + " " + message + " " + border)
    print(line)


def main():
    m = [9, 12, 45]
    print("Before m= ", m)
    modify(m)
    print("After m= ", m)
    replace(m)
    print("After Replace m= ", m)
    update_info(m)
    print("After Update m= ", m)

    # Set parameters in order
    banner("Hello World!","%")
    # Use only required parameters
    banner('WSU')
    # use parameters by name
    banner(border='@', message="Weber State")
    numberf_info()

    # When are default arguments evaluated??


def add_spam(menu=None):
    """
    Add spam to my list
    :param menu: Optional list object
    :return: menu
    """
    if menu is None:
        menu = []
    menu.append("spam")
    return menu


def numberf_info():
    """
    Write a function that prompts the user
    for two integers, then it prints: The sum,
    the difference, the product, the average,
    and the distance(absolute value), the maximum,
    the minimum
    :return:
    """
    print()
    i1 = int(input("Enter first integer"))
    i2 = int(input("Enter second integer"))
    print("%-12s%5d" % ("Sum:", i1 + i2))
    print("%-12s%5d" % ("Difference:", i1 - i2))
    print("%-12s%5d" % ("Product:", i1*i2))
    print("%-12s%8.2f" % ("Average:", (i1 + i2)/2))
    print("%-12s%8.2f" % ("Average:", abs(i1-i2)))
    print("%-12s%5d" % ("Max:", max(i1, i2)))
    print("%-12s%5d" % ("Max:", min(i1, i2)))
    s = i1 + i2
    print("sum = ", s)
    d = i1 - i2
    print("difference = ", d)
    p = i1*i2
    print("product = ", p)
    if i1 <= i2:
        print("Second integer ",i2," is Maximum and first integer ",i1," is Minimum.")
    else:
        print("Second integer ", i2, " is Minimum and first integer ", i1, " is Maximum.")

if __name__ == '__main__':
    main();