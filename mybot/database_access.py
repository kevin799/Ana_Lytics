from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster
from mybot.models import *
from django.http import HttpResponse

'''
Comandos para usar dentro do Cassandra
https://stackoverflow.com/questions/38696316/how-to-list-all-cassandra-tables
'''
def insert():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('bot')
    insert = ExampleModel(description="Funfou essa bagaca!!!!",description2 = 'karai man genial')
    insert.save()
    cluster.shutdown()

def save_conversation_flow(id,json):
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('bot')
    insert  = CfConversationFlow(cf_id_work = id,cf_json = json.replace("'",'"'))
    insert.save()
    cluster.shutdown()