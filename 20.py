# Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]
class elements:
    def sum_zero(self,list1):
        list=[]
        for items in list1:
            for item in list1:
                for ite in list1:
                    if items!=item!=ite and items+item+ite==0:
                        list2=[items,item,ite]
                        list2.sort()
                        if list2 not in list:
                            list.append(list2)
        return list

print(elements().sum_zero([-25, -10, -7, -3, 2, 4, 8, 10]))