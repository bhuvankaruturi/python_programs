def comparator(n):
    n_100 = 100 * n * n
    twoPowerN = 2 ** n
    if n_100 < twoPowerN:
        print("100 * n ^ 2 is :",n_100)
        print("2 to the power of n is :",twoPowerN)
    return n_100 < twoPowerN

#program execution starts here
x = 0
while True:
    x += 1
    if comparator(x):
        print("n value is :",x)
        break