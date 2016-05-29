def fibonacci(n):
    #create array
    F = [0,1]

    for i in range(2, n+1):
        F.append((F[i-1] + F[i-2]) % 10)
    return F[n]

print fibonacci(100000000);
