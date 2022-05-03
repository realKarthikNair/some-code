#!/usr/bin/python3

x,y = map(int,input("Enter x and y separated with space\n").split())

if (y/x).is_integer()!=True:
    a,b=0,0

elif (x==y): a,b=1,1

else:
    for i in range(2, y+1):
        j=1 
        while ((i**j)<= y):
            if (i**j)==int(y/x):
                b,a=i,j
                break
            j+=1        
        if "b" in globals(): break
  
print(a,b, sep=" ")


        
