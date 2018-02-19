#! /usr/bin/env python2
def bluemoonsinrange(day, year, end):
    blue_moons = 0
    last_moon_month = "starting Value"
    while(year <= end):
        if getmonth(day) == last_moon_month:
            blue_moons += 1
        if day >= 366:
            day -= 365
            year += 1
        last_moon_month = getmonth(day)
        day += 29.530588
    print(blue_moons)
    return(blue_moons)


def getmonth(day):
    months = {(0, 31): "January", (32, 59): "Febuary", (60, 90): "March",
              (91, 120): "April", (121, 151): "May", (152, 181): "June",
              (182, 212): "July", (213, 243): "August", (244, 273): "September",
              (274, 304): "October", (305, 335): "November",
              (336, 365): "December"}
    for month in months.iterkeys():
        if month[0] <= day <= month[1]:
            return months[month]


assert bluemoonsinrange(2.1, 2018, 2039) == 11, "Not right"
