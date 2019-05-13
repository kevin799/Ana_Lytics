# example/models.py
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

'''
Antes de rodar a sincronização do banco de dados Cassandra deve se rodar seguinte comando:
pip install django-cassandra-engine
https://pypi.org/project/django-cassandra-engine/

Neste arquivo podemos fazer a criação de tabela dentro do banco de dados cassandra,
onde todos os dados inseridos serão tratados como objetos.
Onde para cada mudança ocorrida no codigo basta rodar o seguinte comando para a sincronização das
tabelas contidas no banco: python manage.py sync_cassandra

Site referencia: https://www.slothparadise.com/how-to-install-and-use-cassandra-on-django/

'''

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
