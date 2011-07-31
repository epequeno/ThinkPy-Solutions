# Run this version of fibonacci and the original with a range of parameters
# and compare their run times.

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    else:
        res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res

#def fibonacci(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else: 
#        return fibonacci(n - 1) + fibonacci(n - 2)

print fibonacci(40)

# New version:
#n = 20
#real	0m0.015s
#user	0m0.004s
#sys	0m0.012s

#n = 30
#real	0m0.016s
#user	0m0.012s
#sys	0m0.004s

#n = 40
#real	0m0.017s
#user	0m0.008s
#sys	0m0.008s

# Old version:
#n = 20
#real	0m0.026s
#user	0m0.008s
#sys	0m0.020s

#n = 30
#real	0m0.525s
#user	0m0.516s
#sys	0m0.008s

#n = 40
#real	1m0.426s
#user	1m0.404s
#sys	0m0.012s