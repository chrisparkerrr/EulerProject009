number = 1000

def getfactorpairs(r, n): # generate pythagorean triples based on seed r
    factorpair = []
    tmp = (r**2)/2
    for i in range(1, int(tmp)+1):
        if tmp % i == 0 and i + int(tmp/i) <= n:  # only adds if tuple sum is less than n
            factorpair.append([i, int(tmp/i)])
    del factorpair[int(len(factorpair)/2):len(factorpair)] #clean repeated factors
    return factorpair

def findabc(n):  # n is the number in which a + b + c = n
    r = 2
    comparisons = 0
    while len(getfactorpairs(r, n)) > 0:
        f = getfactorpairs(r, n)
        for i in f:  # uses every seed
            k = 1
            a = i[0] + r
            b = i[1] + r
            c = i[0] + i[1] + r
            while k*(a + b + c) <= n:
                comparisons += 1
                if k*(a + b + c) == n:
                    solution = "\n{\n a^2 + b^2 = c^2\n a + b + c = %d\n}\n" \
                               "Solution:\na = %d\nb = %d\nc = %d\na*b*c = %d"\
                               % (n, k*a, k*b, k*c, k*a*k*b*k*c)
                    return solution
                k += 1
        r += 2
    return "There's no a, b, c such that\n{\n a^2 + b^2 = c^2\n a + b + c = %d\n}" % n

print(findabc(number))
