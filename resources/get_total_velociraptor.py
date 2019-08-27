from flask import request,jsonify, Response 
from flask_restful import Resource
import datetime
import dateutil
from datetime import timedelta
import dateutil.parser as parser
from data_store.load_data import LoadData
from util.date_time_util import DateTimeUtil


class GetTotalVelociraptor(Resource):
    def get(self):
        
        datestring = request.args['x']
        sum = 0
        util = DateTimeUtil()
        date_range_list = util.create_year_range(datestring)
        # Getting min and max date range from +/- 3 years range
        min_year = min(date_range_list)
        max_year = max(date_range_list)
        
        # Iterating through +/- 3 years date range
        for date_range in date_range_list:

            iso_date_range = parser.parse(date_range).isoformat()
            # Extracting year from date range for checking whether its present in the store
            year = parser.parse(iso_date_range).year

            #If year is present in Data store we iterate through its month check for all values of total velociraptor
            if(year in LoadData.get_store_data().year_dict):
                year_store = LoadData.get_store_data().year_dict[year]
                # Iterating month by month
                for month in range(1,13):
                    # Checking if given month is present for given year
                    if(month in year_store.month_dict):
                        month_stores =  year_store.month_dict[month]
                        # Iterating through different dates present in given month and year
                        for month_store in month_stores:
                            # Checking if given date of month is our range of min and max date range
                            if(month_store.time >= min_year and month_store.time <= max_year):
                                sum+= int(month_store.total_velociraptor)
        return sum


