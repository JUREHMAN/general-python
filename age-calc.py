d1 = int(input("Please Enter the date of your birthday(only the day):\n"))
m1 = int(input("Please Enter the month of your birthday:\n"))
y1 = int(input("Please Enter the year of your birthday:"))

def func(d1,m1,y1):
    d2 = int(input("Please Enter the current date(only the day):\n"))
    m2 = int(input("Please Enter the current month:\n"))
    y2 = int(input("Please Enter the current year:\n"))
    y = y2 - y1
    m = abs(m2 - m1)
    d = abs(d2 - d1)
    nod = y * 365 + m * 30 + d
    print("Your age is ",y," years")
    print("Your age in days is ",nod)
func(d1,m1,y1)