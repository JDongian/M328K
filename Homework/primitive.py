x = int(raw_input("Find primitive root for: "))

def primes(n):
    primfac = set([])
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.add(d)
            n /= d
        d += 1
    if n > 1:
        primfac.add(n)
    return primfac

def is_coprime(a, b):
    for p in primes(min(a,b)):
        if max(a,b)%p == 0:
            return False
    return True

def is_complete(g, x):
    complete_mult_group = set(range(1,x))
    for e in list(complete_mult_group):
        if not is_coprime(e, x):
            complete_mult_group.remove(e)
    return g == complete_mult_group

roots = []
for i in xrange(2,x):
    group = set([])
    for j in xrange(1,x):
        result = (i**j)%x
        if not result in group:
            group.add(result)
        else:
            break
    if is_complete(group, x):
        roots.append(i)
print roots
