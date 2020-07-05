# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?

list1=[]
print(id(list1))

x=int(input("how many friends :"))
for i in range(x):
    y=str(input())
    list1.append(y)

print(id(list1))

#the id of the list doesnt change

print(list1)

list1.sort()

print(list1)

