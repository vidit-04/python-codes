def power(b,p):
    y=b**p
    return y
def calcSquare(x):
    a=power(x,2)
    return a
n=int(input())
result=calcSquare(n)+power(n,3)
print(result)