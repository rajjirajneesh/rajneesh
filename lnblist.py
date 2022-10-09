L1=[11,21,24,12,18]
L2=[14,44,25,37,13]
print('L1=',L1)
print('L2=',L2)
L3=[]
odd=[]
even=[]
for i in range(len(L1)):
    if i%2!=0:
        odd.append(L1[i])
for i in range(len(L2)):
    if i%2==0:
        even.append(L2[i])
        L3=odd+even
print('L3=',L3)
        
    
