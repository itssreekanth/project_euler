def fibonacci(x):
    first = 1
    second = 1
    sum = 0
    while first<x:
        first,second = second, first+second
        if first%2==0:
            sum+=first
    return sum

fibonacci(4000000)
