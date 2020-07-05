# Write an if statement to determine whether a variable holding a year
# is a leap year.

def leap_year(year_date):
    if (year_date%4==0):
        if(year_date%100==0):
            if(year_date%400==0):
                print("{} is a leap year".format(year_date))
            else:
                print("{} is not a leap year".format(year_date))
        else:
            print("{} is a leap year".format(year_date))
    else:
        print("{} is not a leap year".format(year_date))




x=int(input("give the year you want to check :"))

leap_year(x)