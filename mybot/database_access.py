from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster
from mybot.models import *
from django.http import HttpResponse
import datetime
from django.core.exceptions import ObjectDoesNotExist

'''
Comandos para usar dentro do Cassandra
https://stackoverflow.com/questions/38696316/how-to-list-all-cassandra-tables

Comando para acesso ao banco:
>cqlsh localhost

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
'''
def save_usuario():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('bot')
    insert  = UsuUSuario(usu_id_workplace='123456',usu_nome='teste',usu_apelido='teste',usu_email='teste@email.com',usu_ultima_interacao=datetime.datetime.now())
    insert.save()
    cluster.shutdown()
'''

def count_usuario(usu_id):
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('bot')
    rows = session.execute("select count(*) from usu_usuario where usu_id_workplace = %s;"%usu_id)
    for user_row in rows:
        count=user_row.count
    return count

def usu_usuario(usu_id):
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('bot')
    lista = []
    rows = session.execute("select usu_nome,usu_apelido,usu_email,usu_ultima_interacao from usu_usuario where usu_id_workplace = %s;" % usu_id)
    for user_row in rows:
        nome = user_row.usu_nome
        lista.append(nome)
        apelido = user_row.usu_apelido
        lista.append(apelido)
        email = user_row.usu_email
        lista.append(email)
        ultimo_acesso = user_row.usu_ultima_interacao
        lista.append(ultimo_acesso)
    return lista

'''
O cadastro do Usuario somente vai funcionar caso execute o projeto inteiro do Django, pois nela requer o acesso a settings para que possa utilizar as funoes 
de Model do Django.
'''

def cadastro_usuario(usu_id,usu_nome,usu_apelido,usu_email):
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('bot')
    usuario = usu_usuario(usu_id)

    if(count_usuario(usu_id)==0):
        insert = UsuUSuario(usu_id_workplace=usu_id,usu_ultima_interacao=datetime.datetime.now())
        insert.save()
        cluster.shutdown()
        return
    if(usuario[0] is None):
        session.execute("update usu_usuario set usu_nome = '%s' where usu_id_workplace = %s"%(usu_nome,usu_id))
        cluster.shutdown()
        return
    if (usuario[1] is None):
        session.execute("update usu_usuario set usu_apelido = '%s' where usu_id_workplace = %s" % (usu_apelido,usu_id))
        cluster.shutdown()
        return
    if (usuario[2] is None):
        session.execute("update usu_usuario set usu_email = '%s' where usu_id_workplace = %s" % (usu_email, usu_id))
        cluster.shutdown()
        return




'''
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.set_keyspace('bot')
rows = session.execute("select count(*) from usu_usuario where usu_id_workplace = %s ;"%123457)

for user_row in rows:
    print(user_row.count)usu_nome(usu_id) 
'''
#print(count_usuario(123))
#print(cadastro_usuario(123,None,None,None))
#print("update usu_usuario set usu_nome = '%s' where usu_id_workplace = %s"%('teste',123))
'''************************************MYSQL*********************************************************'''

def existecia_usuario(id):
    try:
        return (Usuario.objects.get(id=id)!=None)
    except ObjectDoesNotExist:
        return False

def cadastro_usuario(id,texto):
    if(existecia_usuario(id)):
        usuario = Usuario.objects.get(id=id)
        if(usuario.email== None):

            if('@' in texto):

                try:
                    colaborador = Colaboradores.objects.get(email = texto)
                    usuario.nome = colaborador.nome
                    usuario.email = colaborador.email
                    usuario.save()
                    print('entrou no save do usuario')
                    return
                except ObjectDoesNotExist:
                    usuario.email = texto
                    usuario.save()
                    print('entrou na excessao')
                    return


