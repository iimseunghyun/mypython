
import datetime

dt = datetime.datetime.now()

if dt.weekday() == 1:
    print("today is Tuesday!")

elif dt.weekday() == 0:
    print ('today is Monday!')

elif dt.weekday() == 2:
    print ('today is Wednesday!')

elif dt.weekday() == 3:
    print ('today is Thursday!')

elif dt.weekday() == 4:
    print ('today is Friday!')

elif dt.weekday() == 5:
    print ('today is Saturday!')

elif dt.weekday() == 6:
    print ('today is Sunday!')

