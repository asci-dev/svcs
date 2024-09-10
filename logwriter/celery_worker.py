import datetime
import environ
from celery import Celery
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Celery('log', broker='pyamqp://guest@localhost//')

env = environ.Env()
env.read_env()

@app.task()
def write_logitem(application, logmessage):
    now = datetime.datetime.now()
    uri = env('MONGODB_URL')
    client = MongoClient(uri, server_api=ServerApi('1'))
    subscription_db = client["Subscription"]
    logitem_col = subscription_db["subscription_logitem"]

    logitem_col.insert_one({
        'time': now.strftime('%Y-%m-%d %H:%M:%S'),
        'app': application,
        'logmessage': logmessage
    })

    return 'Log message entered'