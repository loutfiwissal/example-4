N=int(input('Enter a number : '))
S=0
X=1
for i in range(N):
    S=S+(X**2)
    X=X+2
print(" the result is",S)
