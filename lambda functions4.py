#create a list [(1,2),(3,4),(5,6)] and use a lambda function to multiply the first and second elements of each tuple together

l=[(1,2),(3,4),(5,6)]
x=lambda a:a[0]*a[1]
for i in l :
    print(x(i))
        

   

