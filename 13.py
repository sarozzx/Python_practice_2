# Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22
#
# John,54 Love Ave,21

import csv

def create_csv(fname,list1):
    field=['Name','Address','Age']

    filename=fname+".csv"

    with open(filename,'w') as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow(field)
        csvwriter.writerows(list1)
list=[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
create_csv("firstfile",list)
