import time,datetime
from datetime import date, timedelta,time


#exercice 1

print("****** exercice 1 ******")
print("Date et heure actuelles: " , datetime.datetime.now())
print("Année actuelle:", datetime.date.today().strftime("%Y"))
print("Mois de l'année: ", datetime.date.today().strftime("%B"))
print("Numéro de la semaine de l'année: ", datetime.date.today().strftime("%W"))
print("Jour de la semaine: ", datetime.date.today().strftime("%w"))
print("Jour de l'année: ", datetime.date.today().strftime("%j"))
print("Jour du mois: ", datetime.date.today().strftime("%d"))
print("Jour de la semaine: ", datetime.date.today().strftime("%A"))

#exercice 2

print("****** exercice 2 ******")

dt = date.today() - timedelta(5)
print('Date actuelle:',date.today())
print('5 jours avant la date actuelle:',dt)

#exercice 3

print("****** exercice 3 ******")

from datetime import datetime, time

def date_diff_in_seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def dhms_from_seconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

#Specified date
date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

#Current date
date2 = datetime.now()
print("\n%d days, %d hours, %d minutes, %d seconds" % dhms_from_seconds(date_diff_in_seconds(date2, date1)))








#exercice 4

print("****** exercice 4 ******")



def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False
print(leap_year(2004))
print(leap_year(2018))