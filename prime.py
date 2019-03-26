# code to find prime numbers upto number n
n=int(input())
c=2
print("2")
for num in range(3,n+1):
    if num>1:
         for x in range(2,num):
            if num%x==0:
              break
         else:
             print(num)
            
    
    
    
