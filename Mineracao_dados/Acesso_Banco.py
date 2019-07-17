# -*- coding: utf-8 -*-
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster
import MySQLdb



def get():
    lst= {'usuario':[],
          'json':[],
          'id':[]}
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('bot')
    rows = session.execute('select cf_id_work,cf_json,cf_id from cf_conversation_flow')
    for i in rows:
        lst['usuario'].append(i[0])
        lst['json'].append(i[1])
        lst['id'].append(i[2])
    cluster.shutdown()
    session.shutdown()
    return lst

def mysql_save(dic):
    con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
    cursor = con.cursor()
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('bot')
    qtd = len(dic['usuario']) - 1
    while (qtd != -1):
        cursor.execute("INSERT INTO bot.mybot_mdc_mineracao_dados_cassandra(id_user,json_dados) value (%s,'%s')" %(dic['usuario'][qtd],dic['json'][qtd]))
        session.execute("delete from cf_conversation_flow where cf_id = %s" % (dic['id'][qtd]))
        qtd = qtd - 1
        con.commit()
    con.close()


    cluster.shutdown()
    session.shutdown()

mysql_save(get())