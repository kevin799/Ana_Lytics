# -*- coding: utf-8 -*-
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster
import MySQLdb
import pandas
import json


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
        try:
            cursor.execute("INSERT INTO bot.mybot_mdc_mineracao_dados_cassandra(id_user,json_dados) value (%s,'%s')" %(dic['usuario'][qtd],dic['json'][qtd]))
            session.execute("delete from cf_conversation_flow where cf_id = %s" % (dic['id'][qtd]))
        except:
            pass
        qtd = qtd - 1
        con.commit()
    con.close()


    cluster.shutdown()
    session.shutdown()

mysql_save(get())
'''
con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
cursor = con.cursor()
cursor.execute("select id_user,json_dados,id from bot.mybot_mdc_mineracao_dados_cassandra")
resultado = cursor.fetchall()
for j in resultado:
    js = json.loads(j[1])
    id = j[2]
    i = js['entry'][0]['messaging'][0]
    print(js)
    print('---------------------------------------------------------')
    print(i)
    if ('message' in i.keys() and 'sender' in i.keys() and 'recipient' in i.keys() and 'timestamp' in i.keys()) and (
            'is_echo' not in i['message'].keys() and 'app_id' not in i['message'].keys() and 'sticker_id' not in i[
        'message'].keys() and 'attachments' not in i['message'].keys()):
        for i in js['entry']:
            DSC_BOT_ID = str(i['id'])
            DSC_BOT_TIME = str(pandas.to_datetime((i['time']), unit='ms'))
            DSC_BOT_MESSAGING_SENDER_ID = str(i['messaging'][0]['sender']['id'])
            DSC_BOT_MESSAGING_RECIPIENT_ID = str(i['messaging'][0]['recipient']['id'])
            DSC_BOT_MESSAGING_TIME = str(pandas.to_datetime((i['messaging'][0]['timestamp']), unit='ms'))
            DSC_BOT_MESSAGING_MESSAGE_MID = str(i['messaging'][0]['message']['mid'])
            DSC_BOT_MESSAGING_MESSAGE_SEQ = str(i['messaging'][0]['message']['seq'])
            DSC_BOT_MESSAGING_MESSAGE_TEXT = str(i['messaging'][0]['message']['text'])
        cursor.execute("INSERT INTO bot.mybot_dsc_dados_conversa(DSC_BOT_ID,DSC_BOT_TIME,DSC_BOT_MESSAGING_SENDER_ID,DSC_BOT_MESSAGING_RECIPIENT_ID,DSC_BOT_MESSAGING_TIME,DSC_BOT_MESSAGING_MESSAGE_MID,DSC_BOT_MESSAGING_MESSAGE_SEQ,DSC_BOT_MESSAGING_MESSAGE_TEXT) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"
                       %(DSC_BOT_ID,DSC_BOT_TIME,DSC_BOT_MESSAGING_SENDER_ID,DSC_BOT_MESSAGING_RECIPIENT_ID,DSC_BOT_MESSAGING_TIME,DSC_BOT_MESSAGING_MESSAGE_MID,DSC_BOT_MESSAGING_MESSAGE_SEQ,DSC_BOT_MESSAGING_MESSAGE_TEXT))
        con.commit()

    if ('message' in i.keys() and 'sender' in i.keys() and 'recipient' in i.keys() and 'timestamp' in i.keys()) and (
            'is_echo' in i['message'].keys() and 'app_id' in i['message'].keys()):
        for i in js['entry']:
            DSC_BOT_ID = i['id']
            DSC_BOT_TIME = str(pandas.to_datetime((i['time']), unit='ms'))
            DSC_BOT_MESSAGING_SENDER_ID = (i['messaging'][0]['sender']['id'])
            DSC_BOT_MESSAGING_RECIPIENT_ID = (i['messaging'][0]['recipient']['id'])
            DSC_BOT_MESSAGING_TIME = str(pandas.to_datetime((i['messaging'][0]['timestamp']), unit='ms'))
            DSC_BOT_MESSAGING_MESSAGE_IS_ECHO = (i['messaging'][0]['message']['is_echo'])
            DSC_BOT_MESSAGING_MESSAGE_APP_ID = (i['messaging'][0]['message']['app_id'])
            DSC_BOT_MESSAGING_MESSAGE_MID = (i['messaging'][0]['message']['mid'])
            DSC_BOT_MESSAGING_MESSAGE_SEQ = (i['messaging'][0]['message']['seq'])
            DSC_BOT_MESSAGING_MESSAGE_TEXT = (i['messaging'][0]['message']['text'])
        cursor.execute(
            "INSERT INTO bot.mybot_drb_dados_resposta_bot(DSC_BOT_ID,DSC_BOT_TIME,DSC_BOT_MESSAGING_SENDER_ID,DSC_BOT_MESSAGING_RECIPIENT_ID,DSC_BOT_MESSAGING_TIME,DSC_BOT_MESSAGING_MESSAGE_IS_ECHO,DSC_BOT_MESSAGING_MESSAGE_APP_ID,DSC_BOT_MESSAGING_MESSAGE_MID,DSC_BOT_MESSAGING_MESSAGE_SEQ,DSC_BOT_MESSAGING_MESSAGE_TEXT) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
            % (DSC_BOT_ID,DSC_BOT_TIME,DSC_BOT_MESSAGING_SENDER_ID,DSC_BOT_MESSAGING_RECIPIENT_ID,DSC_BOT_MESSAGING_TIME,DSC_BOT_MESSAGING_MESSAGE_IS_ECHO,
               DSC_BOT_MESSAGING_MESSAGE_APP_ID,DSC_BOT_MESSAGING_MESSAGE_MID,DSC_BOT_MESSAGING_MESSAGE_SEQ,DSC_BOT_MESSAGING_MESSAGE_TEXT))
        con.commit()

    if ('delivery' in i.keys() and 'sender' in i.keys() and 'recipient' in i.keys() and 'timestamp' in i.keys()):
        for i in js['entry']:
            DBD_BOT_ID = i['id']
            DBD_BOT_TIME = str(pandas.to_datetime((i['time']), unit='ms'))
            DBD_BOT_MESSAGING_SENDER_ID = str(i['messaging'][0]['sender']['id'])
            DBD_BOT_MESSAGING_RECIPIENT_ID = str(i['messaging'][0]['recipient']['id'])
            DBD_BOT_MESSAGING_TIME = str(pandas.to_datetime((i['messaging'][0]['timestamp']), unit='ms'))
            DBD_BOT_MESSAGING_DELIVERY_MIDS = str(i['messaging'][0]['delivery']['mids'][0])
            DBD_BOT_MESSAGING_DELIVERY_WATERMARK = str(i['messaging'][0]['delivery']['watermark'])
            DBD_BOT_MESSAGING_DELIVERY_SEQ = str(i['messaging'][0]['delivery']['seq'])

        cursor.execute("INSERT INTO bot.mybot_dbd_dados_bot_delivery(DBD_BOT_ID,DBD_BOT_MESSAGING_SENDER_ID,DBD_BOT_MESSAGING_RECIPIENT_ID,DBD_BOT_MESSAGING_DELIVERY_MIDS,DBD_BOT_MESSAGING_DELIVERY_WATERMARK,DBD_BOT_MESSAGING_DELIVERY_SEQ,DBD_BOT_TIME,DBD_BOT_MESSAGING_TIME) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"
                       %(DBD_BOT_ID,DBD_BOT_MESSAGING_SENDER_ID,DBD_BOT_MESSAGING_RECIPIENT_ID,DBD_BOT_MESSAGING_DELIVERY_MIDS,DBD_BOT_MESSAGING_DELIVERY_WATERMARK,
                         DBD_BOT_MESSAGING_DELIVERY_SEQ,DBD_BOT_TIME,DBD_BOT_MESSAGING_TIME))
        con.commit()
    cursor.execute("DELETE FROM bot.mybot_mdc_mineracao_dados_cassandra WHERE ID = %s" %(id))
    con.commit()
con.close()'''