x1 = lambda a,b: a*2+b
x2 = lambda a,b: a**2+b**2
x3 = lambda a,b: a**2+2*a*b+b**2
x4 =  lambda a : a/3 if a%3==0 else a*2 #doe als waar anders doe
x5 =  lambda a,b : a/2 if a>b*2 else a*2
x6 =  lambda a,b,c : c-(a+b) if a+b < c else a+b+c
print(x1(4,2))
print(x2(3,4))
print(x3(3,4))
print(x4(7))
print(x5(9,12))
print(x6(1,2,9))


