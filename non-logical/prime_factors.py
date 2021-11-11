def factor(n):
    assert n>=2
    factors = []
    fact = 2
    while n>1:
        if n%fact==0:
            factors.append(fact)
            n /= fact
        else:
            fact+=1
    return list(set(factors))

factor(600851475143)
