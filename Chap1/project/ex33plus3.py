n=input("input the times you want to loop:")
n=int(n)
k=input("input the nubmers you want to add:")
k=int(k)
numbers=[]
global i,j
i=0
j=0


for i in range(0,n ):
    print("at he top i is %d" %i )
    j=j+k
    numbers.append(j)
    print("numbers now:" ,numbers)
    print("at the bottom  i is %d" % i )

print('the numbers:')
for num in numbers:
    print (num)
