lst=[]
n=int(input('enter the size of list'))
print('enter the number')
for x in range (n):
    num=int(input())
    lst.append(num)
c=[x for x in lst if x>9]
print('after removing number <9=',c)
s=sum(c)
print('sum of remaining number in list =',s)
