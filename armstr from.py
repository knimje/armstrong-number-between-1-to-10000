#WAP to check if any number entered by th euser is armstrong or not by writing a fuction
for i in range(1,10000):
    sum=0
    j=i
    def count1(i):
        count=0
        while i!=0: 
             i=i//10
             count+=1
        return count

    while j!=0:
        sum +=(j%10)**count1(i)
        j=j//10
    if sum==i:
        print("armstrong num ",i)