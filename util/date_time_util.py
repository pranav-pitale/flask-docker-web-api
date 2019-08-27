import datetime
from datetime import timedelta

class DateTimeUtil(object):

     def create_year_range(self, date):

          format = '%Y-%m-%dT%H:%M:%S%z'
          datestring_object = datetime.datetime.strptime(str(date), format)
          # creating a date range list of -/- 3 years 
          date_range_list = set([str(datestring_object + timedelta(days=i*365)) for i in range(4)]
          +[str(datestring_object - timedelta(days=i*365)) for i in range(4)])

          return date_range_list