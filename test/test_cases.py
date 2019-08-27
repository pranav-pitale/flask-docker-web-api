import pytest
from data_store.load_data import LoadData
from util.date_time_util import DateTimeUtil

def test_load_data():
    LoadData().load()
    year_store = LoadData.year_store_data
    assert(year_store.year_dict[2014].month_dict[11][0].total_velociraptor,4)

def test_date_util():
    date = DateTimeUtil().create_year_range('2014-11-06T19:02:17-08:00')
    print(len(date))
    assert(len(date),7)