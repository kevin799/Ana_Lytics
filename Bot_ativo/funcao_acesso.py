import MySQLdb
from messenger_api import *
from datetime import datetime
import pytz

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


def retorna_admins_analytics():
    con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
    cursor = con.cursor()
    cursor.execute("SELECT 	A.id FROM bot.mybot_usuario A join bot.mybot_role B on A.role_id = B.id join bot.mybot_area C on A.area_id = C.id WHERE B.role = 'ADMIN' AND C.setor = 'ANALYTICS'")
    lista_usuario = []
    resultado = cursor.fetchall()
    for i in resultado:
        lista_usuario.append(i[0])
    con.commit()
    con.close()
    return lista_usuario

def consulta_confirmacao_relatorio(descricao,fbid):
    con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
    cursor = con.cursor()
    cursor.execute("SELECT A.flag_confirmacao FROM bot.mybot_confirmacao_relatorio A JOIN bot.mybot_imagem_relatorio B ON A.imagem_id = B.id WHERE A.usuario_id = %s and data = (select MAX(data) from bot.mybot_imagem_relatorio) and B.descricao = '%s'"%(fbid,descricao))
    resultado = cursor.fetchall()
    flag_confirmacao = 0
    for i in resultado:
        flag_confirmacao = i[0]
    con.commit()
    con.close()
    return flag_confirmacao

def atualiza_confirmacao_relatorio(descricao,id_usuario,num):
    con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
    cursor = con.cursor()
    cursor.execute("update mybot_confirmacao_relatorio set flag_confirmacao = %s where usuario_id = %s and imagem_id = (select id from bot.mybot_imagem_relatorio where descricao = '%s' and data = (select MAX(data) from bot.mybot_imagem_relatorio) )"%(num,id_usuario,descricao))
    con.commit()
    con.close()
    return

def status_ativo_de_acordo(id_usuario):
    con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
    cursor = con.cursor()
    cursor.execute(("update mybot_usuario_funcao set ativo = 1 where id_funcionalidade_id = (select id from bot.mybot_funcionalidades_bot where nome = 'De acordo Painel de bordo') and id_usuario_id = %s") %id_usuario)
    con.commit()
    con.close()


def retorna_basic_analytics():
    con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
    cursor = con.cursor()
    cursor.execute("SELECT 	A.id FROM bot.mybot_usuario A join bot.mybot_role B on A.role_id = B.id join bot.mybot_area C on A.area_id = C.id WHERE B.role = 'BASIC' AND C.setor = 'ANALYTICS'")
    lista_usuario = []
    resultado = cursor.fetchall()
    for i in resultado:
        lista_usuario.append(i[0])
    con.commit()
    con.close()
    return lista_usuario

def update_relatorio_imagem():
    con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
    cursor = con.cursor()
    cursor.execute("SELECT Max(id)id FROM bot.mybot_imagem_relatorio WHERE data = (select max(data) from bot.mybot_imagem_relatorio) and descricao ='Painel de bordo'")
    resultado = cursor.fetchall()
    id = 0
    for i in resultado:
        id= i[0]
    cursor.execute("update bot.mybot_imagem_relatorio set enviado = 2 where id = %s"%id)
    con.commit()
    con.close()
    return

def confirmacao_de_todos_os_admins():
    contador = 0
    con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
    cursor = con.cursor()
    cursor.execute(
        "SELECT enviado,usuario_id,MAX(A.id)id FROM mybot_confirmacao_relatorio A join bot.mybot_imagem_relatorio B ON A.imagem_id = B.id join bot.mybot_usuario C ON A.usuario_id = C.id join bot.mybot_role D ON C.role_id = D.id join bot.mybot_area E on C.area_id = E.id where B.descricao = 'Painel de bordo' and B.data = (select max(data) from bot.mybot_imagem_relatorio) and role = 'ADMIN' and setor = 'ANALYTICS' group by enviado,usuario_id")
    resposta = cursor.fetchall()
    lista = {'enviado': [], 'usuario': []}
    for i in resposta:
        lista['enviado'].append(i[0])
        lista['usuario'].append(i[1])

    for i in lista['enviado']:
        contador = contador + i
    #Caso tenha enviado uma vex, ela nao envia mais, pois é atualizada fara flag =2 quando está totalmente certo
    if len(lista['enviado']) == contador:
        return True
    else:
        return False

def conversor_hora(x,y):
    if(x=='01:00' and y =='AM'):
        return '01:00'
    if (x == '02:00' and y == 'AM'):
        return '02:00'
    if (x == '03:00' and y == 'AM'):
        return '03:00'
    if (x == '04:00' and y == 'AM'):
        return '04:00'
    if (x == '05:00' and y == 'AM'):
        return '05:00'
    if (x == '06:00' and y == 'AM'):
        return '06:00'
    if (x == '07:00' and y == 'AM'):
        return '07:00'
    if (x == '08:00' and y == 'AM'):
        return '08:00'
    if (x == '09:00' and y == 'AM'):
        return '09:00'
    if (x == '10:00' and y == 'AM'):
        return '10:00'
    if (x == '11:00' and y == 'AM'):
        return '11:00'
    if (x == '12:00' and y == 'AM'):
        return '12:00'
    if (x == '01:00' and y == 'PM'):
        return '13:00'
    if (x == '02:00' and y == 'PM'):
        return '14:00'
    if (x == '03:00' and y == 'PM'):
        return '15:00'
    if (x == '04:00' and y == 'PM'):
        return '16:00'
    if (x == '05:00' and y == 'PM'):
        return '17:00'
    if (x == '06:00' and y == 'PM'):
        return '18:00'
    if (x == '07:00' and y == 'PM'):
        return '19:00'
    if (x == '08:00' and y == 'PM'):
        return '20:00'
    if (x == '09:00' and y == 'PM'):
        return '21:00'
    if (x == '10:00' and y == 'PM'):
        return '22:00'
    if (x == '11:00' and y == 'PM'):
        return '23:00'
    if (x == '12:00' and y == 'PM'):
        return '24:00'

def mensagem_comunicado_geral():
    con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
    cursor = con.cursor()
    mensagem = ''
    utcmoment_naive = datetime.utcnow()
    utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)
    localDatetime = utcmoment.astimezone(pytz.timezone('America/Sao_Paulo'))
    data_e_hora_atuais = localDatetime
    cursor.execute("SELECT mensagem,data_envio,horas,periodo FROM bot.mybot_comunicado_geral A join bot.mybot_periodo B on A.periodo_id = B.id join bot.mybot_lista_horas C on A.hora_envio_id = C.id")
    resposta = cursor.fetchall()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:00')
    for i in resposta:
        if(i[1]==datetime.now().date()):
            if(conversor_hora(i[2],i[3])==data_e_hora_em_texto):
                mensagem = i[0]
    con.commit()
    con.close()
    return mensagem

def todos_os_usuarios():
    con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
    cursor = con.cursor()
    usuario = []
    cursor.execute("SELECT distinct id FROM bot.mybot_usuario")
    resposta = cursor.fetchall()
    for i in resposta:
        usuario.append(i[0])
    con.commit()
    con.close()
    return usuario