
def gcd_e(a,b):
    while( a != 0):
        (a,b) = (b%a, a)
    return b
