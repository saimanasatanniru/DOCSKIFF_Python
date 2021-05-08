# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import datetime
import calendar
from calendar import monthcalendar, SATURDAY
    
def intervals(start, end):
    start_date = datetime.datetime.strptime(start, '%Y%m%d')
    end_date = datetime.datetime.strptime(end, '%Y%m%d')
    delta = datetime.timedelta(days=1)
    while start_date <= end_date:
        start_date_new = start_date.strftime('%Y%m%d')
        day = findDay(start_date_new)
        fourth_saturday = fourthSaturday(datetime.datetime.strptime(start_date_new, '%Y%m%d'))
        if(fourth_saturday ^ (day == "Saturday" and int(start_date_new) % 5 == 0)):
            print(start_date_new)
        start_date += delta
        
POSSIBLE_DAYS = set(range(22, 28 + 1))

def fourthSaturday(date):
    return date.weekday() == SATURDAY and date.day in POSSIBLE_DAYS
    
    
def findDay(date):
    day = datetime.datetime.strptime(date, '%Y%m%d').weekday()
    return (calendar.day_name[day])
    
startDate = '20180728'
endDate = '20180927'
intervals(startDate, endDate)