"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

months_w_31 = [1,3,5,7,8,10,12]
months_w_30 = [4,6,9,11]

def what_weekday(weekday):
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    return days[weekday-1]


def month_has_days(day, month, year):
    """This returns true if the month has that amount of days or more (It returns false if month=2 and days=30). It also returns false if day<1"""
    if month in months_w_31:
        return day<=31 and day>0
    elif month in months_w_30:
        return day<=30 and day>0        
    elif month == 2:
        if is_leap(year):
            return day>0 and day<=29
        else:
            return day>0 and day<=28
    else:
        print("Month must be a number between 1 and 12, both included")
        return Null


def is_leap(year):
    """This function returns true if the year is a leap year"""
    if (year % 4 == 0) and (not(year % 100 == 0) or (year % 400 == 0)):
        return True
    else:
        return False





class Date:
    """This class represents a day in its dd/mm/yyyy format"""
    
    def __init__(self, day, month, year, weekday):
        if month_has_days(day, month, year) and weekday > 0 and weekday <= 7:
            self.day = day
            self.month = month
            self.year = year
            self.weekday = weekday
        else:
            print("The date was not created, it is likely that the date does not exist.")
    
    def next_weekday(self):
        """This class moves the weekday one day forward in the future, if it's monday then it will be tuesday, if it's saturday then sunday (weeks start at sunday so sunday is weekday 1)"""
        if self.weekday < 7:
            self.weekday += 1
        else:
            self.weekday = 1
    
    def next_day(self):
        """This class moves the date 1 day in the future, so if the date is feb 3rd, 2020, the date will then be feb 4th, 2020"""
        if month_has_days(self.day + 1, self.month, self.year):
           self.day += 1
        elif self.month<12:
            self.day = 1
            self.month += 1
        else:
            self.day = 1
            self.month = 1
            self.year += 1
        self.next_weekday()
    
    def print_date(self):
        print (f"The date is {self.day}/{self.month}/{self.year} and it's weekday {what_weekday(self.weekday)}")

    
#I now need to create the date on jan 1, 1900, use next_day() to get to jan 1, 1901, then start counting the amount of sundays
#that fell on the 1st of the month until 31 dec 2000.

d = Date(1,1,1900,2)
d.print_date()
while (d.year<1901):
    d.next_day()
d.print_date()

sun_counter = 0
while (d.year<2001):
    if d.weekday == 1 and d.day == 1:
        sun_counter += 1
    d.next_day()
d.print_date()

print(f"There were {sun_counter} sundays in the 20th century")