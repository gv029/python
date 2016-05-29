def euclidGCD(a,b):
    if b == 0:
        return a;
    a_prime = a%b
    return euclidGCD(b,a_prime)

print euclidGCD(28851538,1183019)
