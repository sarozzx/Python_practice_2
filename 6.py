# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

list1=[]
k=int(input("How many friends are there "))
for i in range(k):
    x=input()
    list1.append(x)
y=0
for items in list1:
    if items=="John":
        print("there is a john in your friend list")
        y=1
        break
if y==0:
    print("Not found")