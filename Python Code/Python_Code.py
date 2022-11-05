x=int(input())
k=0
for i in range (2,x):
    if x%i==0:
        k=0
        break
    else:
        k=1 
        

if k==1:
    print("PRIME")
else:
    print("NOT PRIME")


    


