import calendar
cal = calendar.TextCalendar()
cal.pryear(2012)

#1B start on Thursday
cal = calendar.TextCalendar(3)
cal.pryear(2012)


#C
cal = calendar.TextCalendar(6)
cal.prmonth(2018,8)

#D
d = calendar.LocaleTextCalendar(6)
d.pryear(2012)

#E
print(calendar.isleap(2016))
#it expects a year
#it returns true or false
#