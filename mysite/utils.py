from pymongo import MongoClient
import pprint


def get_db_handle(string, db_name):
    client = MongoClient(string)
    return client



string="mongodb+srv://adri_pv:qazxswedc21324354@easy.yvxgjtg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(string)


dbname = client.easy_db



tabla = dbname.easy_t

datos = tabla.find({})

for dato in datos:
    pprint.pprint(dato)




