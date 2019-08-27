from flask import Blueprint
from flask_restful import Api
from data_store.load_data import LoadData
from resources.get_total_velociraptor import GetTotalVelociraptor
from resources.update_velociraptor import UpdateVelociraptor

api_bp = Blueprint('api',__name__)
api = Api(api_bp)
load_object = LoadData()
load_object.load()

# Route Configuration
api.add_resource(GetTotalVelociraptor, '/GetTotalVelociraptor')
api.add_resource(UpdateVelociraptor,'/UpdateVelociraptor')