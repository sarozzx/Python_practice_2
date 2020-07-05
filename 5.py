# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

x=("Ram","Karki",24)

list1=[]
list1.append(x)

a=("ram","thapa",23)
b=("Hari","pandit",25)
c=("Sita","katwal",21)
d=("maniram","gosai",19)

list1.append(a)
list1.append(b)
list1.append(c)
list1.append(d)


print(list1)

list1.sort(key=lambda x:x[2])

print("sorted according to age :",list1)