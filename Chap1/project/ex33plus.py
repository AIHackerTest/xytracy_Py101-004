i=0
numbers=[]
print("input times that you want to loop:" )
n=input()
n=int(n )
print("input the number you want to plus ")
k=input()
k=int(k)

def while_func(n ):
    global i
    while i<n :
        pass
        print("at the top i is %d" %i )
        numbers.append(i)
        i=i+k
        print("numbers now:",numbers)
        print("at the bottom i is %d" %i )


while_func(n )
