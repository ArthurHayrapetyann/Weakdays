Day = int(input("Day  "))
Month = int(input("Month  "))
Year = int(input("Year  "))
def check(Day,Month,Year):       #checks if the date is true
    if Month>12:
        print("Year has 12 month")
        return False
    elif Month%2!=0 and Day>31:
        print("This month has 31 days")
        return False
    elif Month%2==0 and Month!=2 and Month!=8 and Day>30:
        print("This month has 30 days")
        return False
    elif Year%4==0 and Month==2 and Day>29:
        print("This month has 29 days")
        return False
    elif Year%4!=0 and Month==2 and Day>28:
        print("THis month has 28 days")
        return False
    else:
        return True 
def count(Day,Month,Year): #count all days begin 1.jan.1900
    leapyears=Year/4
    Days31=Month/2+1
    years=Year-1900
    if Month>2:
        if Month>8:
            Days=leapyears+((Year-1901)*365)+30+((Days31-1)*31)+((Month-Days31-1)*30)+Day
        else:
            Days=leapyears+((Year-1901)*365)+29+((Days31-1)*31)+((Month-Days31-1)*30)+Day
    else:
        if years%4==0:
            Days=leapyears-1+((Year-1901)*365)+((Days31-1)*31)+Day
        else:
            Days=leapyears+((Year-1901)*365)+((Days31-1)*31)+Day
    Weakday=int(Days%7)
    return Weakday
def Print(Weakday): #count weakday by balance
    if Weakday==0:
        print("Monday")
    elif Weakday==1:
        print("Tuesday")
    elif Weakday==2:
        print("Wednesday")
    elif Weakday==3:
        print("Thursday")
    elif Weakday==4:
        print("Friday")
    elif Weakday==5:
        print("Saturday")
    elif Weakday==6:
        print("Sunday")  
    else:
        raise ValueError()
    return 0  
if check(Day,Month,Year)==True: #call functions
    Print(count(Day,Month,Year))


