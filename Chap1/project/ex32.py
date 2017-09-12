the_count=[1,2,3,4]
fruits=['apples','oranges' ,'pears']
change=[1,'pennies',2,'dimes',3,'quarters']

#this first kind of for-loop goes throught a list
for number in the_count:
    print ("this is count %d" % number)

#same as  above
for fruit in fruits:
    print("a fruit of type %s" %fruit)

#also we can go through mixed lists thorough
#notice we have to use %r since we don't know what's init
for i in change:
    print("i got %r"  % i)

#we can also build lists, first start with an empty one
elements=[]

#then use the range function to do 0 to 5 counts
for i in range(0,6):
    print("adding %r to the list."  % i)
    #append is a funciton that lists understan
    elements.append(i )

#now we can print them out too
for i in elements:
    print("elements was: %d " %i)
