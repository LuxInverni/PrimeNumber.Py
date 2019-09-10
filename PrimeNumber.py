n = 1
while n < 1000:
    for i in range(2, n):    #i is all numbers between 2 and the number being checked
        if (n % i) == 0:    #if n has no remainder/ is divisible by i then it is not a prime
            n=n+1
    else:
        print(f"{n} is a Prime Number")
        n=n+1
