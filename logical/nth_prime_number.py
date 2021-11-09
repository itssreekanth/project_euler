from math import ceil,log
def primes(limit):
    nums = [True]*(limit+1)
    nums[0] = nums[1] = False
    for i,is_prime in enumerate(nums):
        if is_prime:
            yield i
            for k in range(i*i,limit+1,i):
                nums[k] = False
def upper_bound(n):
    if n < 6:
        return 100
    return ceil(n*(log(n)+log(log(n))))
def nth_prime(n):
    p = list(primes(upper_bound(n)))
    return p[n-1]
nth_prime(10**5)
