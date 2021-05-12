# Using normal recursion
def fib_n(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib_n(n - 1) + fib_n(n - 2)


# using memoization
calculated = {}


def fib_m(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n in calculated:
        return calculated[n]
    else:
        calculated[n] = fib_m(n - 1) + fib_m(n - 2)
        return calculated[n]


#print(fib_m(80))

# using for loop

def fib_f(n):
    a,b=0,1
    if n ==0:
        return a
    if n == 1:
        return b
    else:
        for i in range(2,n+1):
            c= a+b
            a=b
            b=c
        return b

print(fib_f(80) == fib_m(80))

