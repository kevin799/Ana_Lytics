import MySQLdb
from messenger_api import *
from datetime import datetime

def get_list_user():
    con = MySQLdb.connect(host = "127.0.0.1",user ="bot",passwd ="#Bot123",db = "bot")
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

def ponto_entrada():
    con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
    cursor = con.cursor()
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:00')
    if(data_e_hora_em_texto == '04:00'):
        cursor.execute("SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '01:00' and periodo_entrada = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '05:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '02:00' and periodo_entrada = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '06:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '03:00' and periodo_entrada = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '07:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '04:00' and periodo_entrada = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '08:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '05:00' and periodo_entrada = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '09:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '06:00' and periodo_entrada = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '10:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '07:00' and periodo_entrada = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '11:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '08:00' and periodo_entrada = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '12:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '09:00' and periodo_entrada = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '13:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '10:00' and periodo_entrada = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '14:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '11:00' and periodo_entrada = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '15:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '12:00' and periodo_entrada = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '16:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '01:00' and periodo_entrada = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '17:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '02:00' and periodo_entrada = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '18:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '03:00' and periodo_entrada = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '19:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '04:00' and periodo_entrada = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '20:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '05:00' and periodo_entrada = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '21:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '06:00' and periodo_entrada = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '22:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '07:00' and periodo_entrada = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '23:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '08:00' and periodo_entrada = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '00:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '09:00' and periodo_entrada = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '01:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '10:00' and periodo_entrada = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '02:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '11:00' and periodo_entrada = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '03:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_entrada = '12:00' and periodo_entrada = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    con.commit()
    con.close()
    return (lista_usuario)

def ponto_ida_almoco():
    con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
    cursor = con.cursor()
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:00')
    if(data_e_hora_em_texto == '04:00'):
        cursor.execute("SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '01:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '05:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '02:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '06:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '03:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '07:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '04:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '08:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '05:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '09:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '06:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '10:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '07:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '11:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '08:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '12:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '09:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '13:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '10:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '14:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '11:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '15:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '12:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '16:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '01:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '17:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '02:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '18:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '03:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '19:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '04:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '20:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '05:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '21:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '06:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '22:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '07:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '23:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '08:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '00:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '09:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '01:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '10:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '02:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '11:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '03:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '12:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    con.commit()
    con.close()
    return (lista_usuario)

def ponto_volta_almoco():
    con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
    cursor = con.cursor()
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:00')
    if(data_e_hora_em_texto == '05:00'):
        cursor.execute("SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '01:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '06:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '02:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '07:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '03:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '08:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '04:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '09:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '05:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '10:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '06:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '11:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '07:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '12:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '08:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '13:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '09:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '14:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '10:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '15:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '11:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '16:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '12:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '17:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '01:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '18:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '02:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '19:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '03:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '20:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '04:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '21:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '05:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '22:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '06:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '23:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '07:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '00:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '08:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '01:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '09:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '02:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '10:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '03:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '11:00' and periodo_almoco = 'PM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    if (data_e_hora_em_texto == '04:00'):
        cursor.execute(
            "SELECT id_usuario_id FROM bot.mybot_usuario_cargo_hora where hora_almoco = '12:00' and periodo_almoco = 'AM';")
        lista_usuario = []
        resultado = cursor.fetchall()
        for i in resultado:
            lista_usuario.append(i[0])
    con.commit()
    con.close()
    return (lista_usuario)

def bater_ponto(fbid):
    fb = FbMessageApi(fbid)
    fb.text_message("Oieee!!! Não esquece de bater o ponto :)!")
    fb.text_message("...")
    envia_print(fbid)

def ida_almoco(fbid):
    fb = FbMessageApi(fbid)
    fb.text_message("Chegou a hora boa!!! Bora encher o buxo!!! AH! Não esquece de bater o ponto ok!")

def volta_almoco(fbid):
    fb = FbMessageApi(fbid)
    fb.text_message("É triste te trazer essa notícia... mas acabou o intervalo 😭... Mas nâo esquece de bater o ponto...")

def envia_print(fbid):
    fb = FbMessageApi(fbid)
    fb.text_message(
        "Futuro painel de bordo!")
    fb.image_message("https://kevinmikio.ngrok.io/static/img/show.jpg")