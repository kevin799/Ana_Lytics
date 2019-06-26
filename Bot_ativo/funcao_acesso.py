import MySQLdb
from messenger_api import *

def get_list_user():
    con = MySQLdb.connect(host = "127.0.0.1",user ="bot",passwd ="bot123",db = "bot")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM bot.mybot_usuario")

    lista_usuario = []
    resultado = cursor.fetchall()
    for i in resultado:
        lista_usuario.append(i[0])

    con.commit()
    con.close()
    return (lista_usuario)

def envio_ola(fbid):
    fb = FbMessageApi(fbid)
    fb.text_message("Estou ativo! mestre")