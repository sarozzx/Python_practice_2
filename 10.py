# Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

def change_cam(str):
    str1=str[0].lower()
    for letter in str[1:]:
        if letter.isupper():
            str1+="_"+letter.lower()
        else:
            str1+=letter
    print("Snake Case: ",str1)
    str2=str1.replace("_","-")
    print("Kebab Case: ",str2)


change_cam("ThisIsCamelCased")
