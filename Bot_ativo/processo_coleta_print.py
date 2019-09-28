# -*- coding: utf-8 -*-
import MySQLdb
from messenger_api import *
from funcao_acesso import *
from datetime import datetime
from funcionalidade_ativo import *

con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
cursor = con.cursor()
cursor.execute("SELECT enviado,usuario_id,MAX(A.id)id FROM mybot_confirmacao_relatorio A join bot.mybot_imagem_relatorio B ON A.imagem_id = B.id join bot.mybot_usuario C ON A.usuario_id = C.id join bot.mybot_role D ON C.role_id = D.id join bot.mybot_area E on C.area_id = E.id where B.descricao = 'Painel de bordo' and B.data = (select max(data) from bot.mybot_imagem_relatorio) and role = 'ADMIN' and setor = 'ANALYTICS' group by enviado,usuario_id")
resposta =cursor.fetchall()
lista = {'enviado':[],'usuario':[]}
for i in resposta:
    lista['enviado'].append(i[0])
    lista['usuario'].append(i[1])

cursor.execute("SELECT data FROM bot.mybot_imagem_relatorio WHERE data = (select max(data) from bot.mybot_imagem_relatorio) and descricao ='Painel de bordo'")
resposta =cursor.fetchall()
for i in resposta:
    print(i)
    hora = i[0]

#Já rodou hj?
if(datetime.now().date() != hora.date()):
    cursor.execute("insert into bot.mybot_imagem_relatorio(data,descricao,enviado) values(NOW(),'Painel de bordo',0)")
    con.commit()
    cursor.execute("insert into bot.mybot_imagem_relatorio(data,descricao,enviado) values(NOW(),'Painel Executivo',0)")
    con.commit()
    cursor.execute("insert into bot.mybot_imagem_relatorio(data,descricao,enviado) values(NOW(),'FPD',0)")
    con.commit()
    cursor.execute("insert into bot.mybot_imagem_relatorio(data,descricao,enviado) values(NOW(),'PDD',0)")
    con.commit()
    cursor.execute("insert into bot.mybot_imagem_relatorio(data,descricao,enviado) values(NOW(),'IPF',0)")
    con.commit()
    for i in lista['usuario']:
        cursor.execute(("update mybot_usuario_funcao set ativo = 1 where id_funcionalidade_id = (select id from bot.mybot_funcionalidades_bot where nome = 'De acordo Painel de bordo') and id_usuario_id = %s") %
                   i)
        con.commit()

#Casos de erro no relatorio
contador = 0
erro = False
for i in lista['usuario']:
    if (lista['enviado'][contador]==-1):
        erro = True
    contador+=1


#Cobrança do de acordo.
if(erro!=True):
    contador = 0
    for i in lista['usuario']:

        if(lista['enviado'][contador] == 0):
            fb = FbMessageApi(i)
            fb.text_message("Favor responder com o seu de acordo!")
            fb.text_message("Painel de bordo")
            fb.image_message("https://kevinmikio.ngrok.io/static/img/SAS.jpg")
            fb.quick_reply_message("Responda o mais rapido o possivel ", [{"content_type": "text",
                                                                           "title": 'Pode enviar!',
                                                                           "payload": 'Pode enviar!'
                                                                           }, {"content_type": "text",
                                                                               "title": 'Ta errado!Arrumar!',
                                                                               "payload": 'Ta errado!Arrumar!'
                                                                               }])
        contador += 1



if (erro):
    cursor.execute("insert into bot.mybot_imagem_relatorio(data,descricao,enviado) values(NOW(),'Painel de bordo',0)")
    con.commit()
    cursor.execute("insert into bot.mybot_imagem_relatorio(data,descricao,enviado) values(NOW(),'Painel Executivo',0)")
    con.commit()
    cursor.execute("insert into bot.mybot_imagem_relatorio(data,descricao,enviado) values(NOW(),'FPD',0)")
    con.commit()
    cursor.execute("insert into bot.mybot_imagem_relatorio(data,descricao,enviado) values(NOW(),'PDD',0)")
    con.commit()
    cursor.execute("insert into bot.mybot_imagem_relatorio(data,descricao,enviado) values(NOW(),'IPF',0)")
    con.commit()
    for i in lista['usuario']:
        cursor.execute((
                           "update mybot_usuario_funcao set ativo = 1 where id_funcionalidade_id = (select id from bot.mybot_funcionalidades_bot where nome = 'De acordo Painel de bordo') and id_usuario_id = %s") %
                       i)
        con.commit()



for i in retorna_admins_analytics():
    if (erro):
        lembrete_erro(i)
    envio_prints_base_validacao(i)



con.close()