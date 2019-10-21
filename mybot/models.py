# -*- coding: utf-8 -*-
# example/models.py
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from django.db import models
'''
Antes de rodar a sincronização do banco de dados Cassandra deve se rodar seguinte comando:
pip install django-cassandra-engine
https://pypi.org/project/django-cassandra-engine/

Neste arquivo podemos fazer a criação de tabela dentro do banco de dados cassandra,
onde todos os dados inseridos serão tratados como objetos.
Onde para cada mudança ocorrida no codigo basta rodar o seguinte comando para a sincronização das
tabelas contidas no banco: python manage.py sync_cassandra

Site referencia: https://www.slothparadise.com/how-to-install-and-use-cassandra-on-django/
--------------------------------------------------------------------------------------------
https://www.codigofluente.com.br/09-criando-e-ativando-models-no-django/
Reeferencia mysql

'''
'''---------------------------------CASSANDRA------------------------------------------------------'''
class ExampleModel(Model):
    read_repair_chance = 0.05 # optional - defaults to 0.1
    example_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    description = columns.Text(required=False)
    description2 = columns.Text(required=False)

class teste2(Model):
    read_repair_chance = 0.05 # optional - defaults to 0.1
    teste_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    description = columns.Text(required=False)

class Person(Model):
    id = columns.UUID(primary_key=True)
    first_name  = columns.Text()
    last_name = columns.Text()

class CfConversationFlow(Model):
    read_repair_chance = 0.05
    cf_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    cf_id_work = columns.Text()
    cf_json = columns.Text()

class UsuUSuario(Model):
    read_repair_chance = 0.05
    #usu_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    usu_id_workplace= columns.Integer(primary_key=True)
    usu_nome = columns.Text()
    usu_apelido = columns.Text()
    usu_email = columns.Text()
    usu_ultima_interacao = columns.DateTime()

class testeUsuUSuario(Model):
    read_repair_chance = 0.05
    #usu_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    usu_id_workplace= columns.Integer(primary_key=True)
    usu_nome = columns.Text()
    usu_apelido = columns.Text()
    usu_email = columns.Text()
    usu_ultima_interacao = columns.DateTime()
'''------------------------------------MYSQL---------------------------------------------------------------------------'''
'''
Formato das colunas :
https://www.webforefront.com/django/modeldatatypesandvalidation.html

Obs: Rodar o comando abaixo caso faça alguma modificação na estrutura da tabela
python manage.py makemigrations mybot
*Depois de rodar o comando acima rodar: 
python manage.py migrate
'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    votes2 = models.IntegerField(default=0)

class Choice_aa(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Area(models.Model):
    setor = models.CharField(max_length=100)


class Role(models.Model):
    role = models.CharField(max_length=100)

class Usuario(models.Model):
    id = models.BigIntegerField(primary_key=True,max_length=None)
    nome = models.CharField(max_length=150,null=True)
    email = models.CharField(max_length=200,null=True)
    status_acesso = models.IntegerField(null=True)
    role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
    area = models.ForeignKey(Area,on_delete=models.CASCADE,null=True)

class Colaboradores(models.Model):
    nome = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200)
    id_area = models.ForeignKey(Area, on_delete=models.CASCADE)
    id_role = models.ForeignKey(Role, on_delete=models.CASCADE,default=1)

class Funcionalidades_bot(models.Model):
    nome = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

class Usuario_Funcao(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_funcionalidade = models.ForeignKey(Funcionalidades_bot, on_delete=models.CASCADE)
    permissao = models.IntegerField(default=1)
    status = models.IntegerField(default=None,null=True)
    ativo = models.IntegerField(null=True)

class Lista_Horas(models.Model):
    horas = models.CharField(max_length=200)

class Conversa_ML(models.Model):
    conversa = models.CharField(max_length=1000)
    resposta = models.CharField(max_length=1000)

class Cargo(models.Model):
    nome = models.CharField(max_length=200)
    horas = models.IntegerField(null=True)

class Usuario_cargo_hora(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE,null=True)
    hora_entrada = models.CharField(max_length=15,null=True)
    periodo_entrada = models.CharField(max_length=10,null=True)
    hora_almoco = models.CharField(max_length=15,null=True)
    periodo_almoco = models.CharField(max_length=10,null=True)

class Funcionalidade_Role_Areas(models.Model):
    id_area = models.ForeignKey(Area, on_delete=models.CASCADE)
    id_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    id_funcionalidade = models.ForeignKey(Funcionalidades_bot, on_delete=models.CASCADE)

class Imagem_Relatorio(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=100)
    enviado = models.IntegerField()

class Confirmacao_relatorio(models.Model):
    imagem = models.ForeignKey(Imagem_Relatorio,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    flag_confirmacao = models.IntegerField()

class Ensino_dialogo(models.Model):
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    pergunta = models.CharField(max_length=500)
    resposta = models.CharField(max_length=500)
    aprovado = models.IntegerField()
    data = models.DateTimeField()


'''------------------Mineracao dados cassandra--------------------------'''

class MDC_Mineracao_Dados_Cassandra(models.Model):
    id_user = models.TextField()
    json_dados= models.TextField()

class Dbd_Dados_Bot_Delivery(models.Model):
    DBD_BOT_ID = models.TextField()
    DBD_BOT_TIME = models.TextField()
    DBD_BOT_MESSAGING_SENDER_ID = models.TextField()
    DBD_BOT_MESSAGING_RECIPIENT_ID = models.TextField()
    DBD_BOT_MESSAGING_TIME = models.TextField()
    DBD_BOT_MESSAGING_DELIVERY_MIDS = models.TextField()
    DBD_BOT_MESSAGING_DELIVERY_WATERMARK = models.TextField()
    DBD_BOT_MESSAGING_DELIVERY_SEQ = models.TextField()

class Dbr_Dados_Bot_Read(models.Model):
    DBR_BOT_ID = models.TextField()
    DBR_BOT_TIME = models.TextField()
    DBR_BOT_MESSAGING_SENDER_ID = models.TextField()
    DBR_BOT_MESSAGING_RECIPIENT_ID = models.TextField()
    DBR_BOT_MESSAGING_TIME = models.TextField()
    DBR_BOT_MESSAGING_READ_WATERMARK = models.TextField()
    DBR_BOT_MESSAGING_READ_SEQ = models.TextField()

class Drb_Dados_Resposta_Bot(models.Model):
    DRB_BOT_ID = models.TextField()
    DRB_BOT_TIME = models.TextField()
    DRB_BOT_MESSAGING_SENDER_ID = models.TextField()
    DRB_BOT_MESSAGING_RECIPIENT_ID = models.TextField()
    DRB_BOT_MESSAGING_TIME = models.TextField()
    DRB_BOT_MESSAGING_MESSAGE_IS_ECHO = models.TextField()
    DRB_BOT_MESSAGING_MESSAGE_APP_ID = models.TextField()
    DRB_BOT_MESSAGING_MESSAGE_MID = models.TextField()
    DRB_BOT_MESSAGING_MESSAGE_SEQ = models.TextField()
    DRB_BOT_MESSAGING_MESSAGE_TEXT = models.TextField()

class Dsc_Dados_Conversa(models.Model):
    DSC_BOT_ID = models.TextField()
    DSC_BOT_TIME = models.TextField()
    DSC_BOT_MESSAGING_SENDER_ID = models.TextField()
    DSC_BOT_MESSAGING_RECIPIENT_ID = models.TextField()
    DSC_BOT_MESSAGING_TIME = models.TextField()
    DSC_BOT_MESSAGING_MESSAGE_MID = models.TextField()
    DSC_BOT_MESSAGING_MESSAGE_SEQ = models.TextField()
    DSC_BOT_MESSAGING_MESSAGE_TEXT = models.TextField()
