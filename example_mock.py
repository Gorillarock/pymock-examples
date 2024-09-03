from datetime import datetime

def is_weekday():
    today = datetime.today()
    print(today)
    # Monday = 0, Sunday = 6
    day_of_the_week = today.weekday()
    print(day_of_the_week)
    return (0 <= today.weekday() < 5)
  
def print_weekday(day):
  print('Today is', '\b' if day else 'not', 'a weekday')
  
weekday = is_weekday()
# make ternaly operator to print 'Yes' if weekday is True, else 'No'
print_weekday(weekday)

#  create a mock for is_weekday which returns False
from unittest.mock import Mock, patch
is_weekday = Mock()
is_weekday.return_value = False
weekday = is_weekday()
print_weekday(weekday)



