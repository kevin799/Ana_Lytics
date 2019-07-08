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

class Usuario(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=150,null=True)
    email = models.CharField(max_length=200,null=True)
    status_acesso = models.IntegerField(null=True)


class Area(models.Model):
    setor = models.CharField(max_length=100)


class Role(models.Model):
    role = models.CharField(max_length=100)

class Colaboradores(models.Model):
    nome = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200)
    id_area = models.ForeignKey(Area, on_delete=models.CASCADE)
    id_role = models.ForeignKey(Role, on_delete=models.CASCADE,default=1)

class Funcionalidades_bot(models.Model):
    nome = models.CharField(max_length=200)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

class Usuario_Funcao(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_funcionalidade = models.ForeignKey(Funcionalidades_bot, on_delete=models.CASCADE)
    permissao = models.IntegerField(default=1)
    status = models.IntegerField(default=0)

