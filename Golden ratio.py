a=int(input('Enter left limit of the interval: '))
b=int(input('Enter the right limit of the interval: '))
r=0.382
t=1-r
E=0.3
def funx(x):
    funx=(x**4)-14*(x**3)+60*(x**2)-70*x
    return funx
while abs(b-a)>E:
    c=a+r*(b-a)
    d=a+t*(b-a)
    fA=funx(a)
    fB=funx(b)
    fC=funx(c)
    fD=funx(d)
    if fC<fD:
        b=d
        fB=fD
        d=c
        fD=fC
        c=a+r*(b-a)
        fC=funx(c)
    else:
        a=c
        fA=fC
        c=d
        fC=fD
        d=a+t*(b-a)
        fD=funx(d)

minimizer=(a+b)/2
print(f'The final interval is: [{a},{b}]')
print(f"Length of final interval is: {b-a}")
print(f'The minimizer of the function is: {minimizer}')
        
