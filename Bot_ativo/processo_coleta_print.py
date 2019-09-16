import MySQLdb
from messenger_api import *
from funcao_acesso import *
from datetime import datetime

con = MySQLdb.connect(host="127.0.0.1", user="bot", passwd="#Bot123", db="bot")
cursor = con.cursor()
cursor.execute("SELECT enviado,usuario_id FROM mybot_confirmacao_relatorio A join bot.mybot_imagem_relatorio B ON A.imagem_id = B.id join bot.mybot_usuario C ON A.usuario_id = C.id join bot.mybot_role D ON C.role_id = D.id join bot.mybot_area E on C.area_id = E.id where B.descricao = 'Painel de bordo' and B.data = (select max(data) from bot.mybot_imagem_relatorio) and role = 'ADMIN' and setor = 'ANALYTICS'")
resposta =cursor.fetchall()
lista = []
for i in resposta:
    lista.append(i[0])
    lista.append(i[1])

cursor.execute("SELECT data FROM bot.mybot_imagem_relatorio WHERE data = (select max(data) from bot.mybot_imagem_relatorio) and descricao ='Painel de bordo'")
resposta =cursor.fetchall()
for i in resposta:
    hora = i[0]

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
    cursor.execute((
                       "update mybot_usuario_funcao set ativo = 1 where id_funcionalidade_id = (select id from bot.mybot_funcionalidades_bot where nome = 'De acordo Painel de bordo') and id_usuario_id = %s") %
                   lista[1])
    con.commit()

if(lista[0] == 0):
    fb = FbMessageApi(lista[1])
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

if (lista[0] == -1):
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
    cursor.execute(("update mybot_usuario_funcao set ativo = 1 where id_funcionalidade_id = (select id from bot.mybot_funcionalidades_bot where nome = 'De acordo Painel de bordo') and id_usuario_id = %s")%lista[1])
    con.commit()

if(lista[0] == 1):
    print('entrou no envio geral')

    for i in retorna_basic_analytics():
        fb = FbMessageApi(i)
        fb.text_message("Painel de bordo")
        fb.image_message("https://kevinmikio.ngrok.io/static/img/SAS.jpg")
    fb = FbMessageApi(100030196033467)
    fb.text_message("Segue o Painel de bordo atualizado")
    fb.image_message("https://kevinmikio.ngrok.io/static/img/SAS.jpg")
    update_relatorio_imagem()
con.close()