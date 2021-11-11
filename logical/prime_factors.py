from math import gcd
def pollard_alg(num):
    def get_factors(n):
        x = 2
        y = 2
        factor = 1
        while factor==1:
            x = (x*x+1)%n
            y = (y**4+2*y*y+2)%n
            factor = gcd(x-y,n)
        return factor
    factors = []
    while num>1:
        next = get_factors(num)
        factors.append(next)
        num //= next
    return factors
pollard_alg(18363797 * 18363799)
