import environ
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

env = environ.Env()
env.read_env()
con = env('MONGODB_URL')
client = MongoClient(con, server_api=ServerApi('1'))
db = client["Subscription"]
col = db["subscription_address"]

address = {
    "name": "Monthy Python",
    "address": "Hardwood Lane",
    "postalcode": "MP1",
    "city": "London",
    "country": "England",
    "email": "monthy@python.com",
}
col.insert_one(address)