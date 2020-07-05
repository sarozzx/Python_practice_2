# Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.

list1=[("ram","thapa",23),("Hari","pandit",25),("Sita","katwal",21),("maniram","gosai",19),("sampurna","acharya",26)]

lst2 = [i[2] for i in list1]
avg=0
for items in lst2:
    avg+=items
avg=avg/len(lst2)

print(avg)

for item in list1:
    print("Name : ",item[0]," ",item[1])
    if(item[2]>avg):
        print("OLD ")
    else:
        print("Young")
