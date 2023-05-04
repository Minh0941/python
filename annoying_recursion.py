
def annoying_factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n==2:
        return 2
    if n ==3:
        return 6
    if n ==4:
        return n*annoying_factorial(n-1)
    if n==5:
        return n*annoying_factorial(n-1)
    if n==6:
        return n*annoying_factorial(n-1)
    if n>6:
        return n*annoying_factorial(n-1)
def annoying_fibonacci(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    if n ==2:
        return 1
    if n==3:
        return 2
    if n==4:
        return annoying_fibonacci(3) + annoying_fibonacci(2)
    if n==5:
        return annoying_fibonacci(4) + annoying_fibonacci(3)
    if n==6:
        return annoying_fibonacci(5) + annoying_fibonacci(4)
    if n>6:
        return annoying_fibonacci(n-1) + annoying_fibonacci(n-2)