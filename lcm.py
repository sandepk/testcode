def find_lcm(n1,n2):
    if n1>n2:
        num=n1
        den=n2
    else:
        num=n2
        den=n1
    rem=num%den
    while(rem!=0):
        num=den
        den=rem
        rem=num%den
    gcd=den
    lcm=int(int(n1*n2)/den)
    return lcm

x = [int(x) for x in input("Enter numbers:").split()] 
n1=x[0]
n2=x[1]
lcm=find_lcm(n1,n2)
for i in range(2,len(x)):
    lcm=find_lcm(lcm,x[i])
print(lcm)