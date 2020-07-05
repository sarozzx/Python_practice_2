# Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid

class checkparen:
    def check(self,mystr):
        open_list=["[","{","("]
        close_list=["]","}",")"]

        stack=[]

        for i in mystr:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                position=close_list.index(i)
                if((len(stack)>0) and open_list[position]==stack[-1]):
                    stack.pop()
                else:
                    return " in a wrong order "

        if len(stack)==0:
            return " in a correct order "
        else:
            return " in a wrong order "

print(checkparen().check("()"))
print(checkparen().check("()[]{}"))
print(checkparen().check("[)"))
print(checkparen().check("({[)]"))
