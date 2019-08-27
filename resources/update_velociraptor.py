from flask import request,jsonify, Response 
from flask_restful import Resource
import dateutil.parser as parser
from data_store.load_data import LoadData
import datetime
from datetime import timedelta
import operator
from util.date_time_util import DateTimeUtil

class UpdateVelociraptor(Resource):

    def post(self):

        request_body = request.get_json()
        time_stamp = request_body['TimeStamp']
        updated_total_velociraptor = request_body['TotalVelociraptor']
        print(time_stamp)
        print(updated_total_velociraptor)
        store = LoadData.get_data_store_for_update(time_stamp)
        if(store):
            store.total_velociraptor = updated_total_velociraptor
        return 1

        