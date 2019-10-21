from mybot.messenger_api import *
from mybot.database_access import *
from mybot.models import *
from django.db.models import Max
import datetime
from mybot.funcoes_bot import *
'''
print('------------Area Teste--------------')
print (consulta_ativo(100030196033467))
print('--------------------------')
print(consulta_status(100030196033467, 'Bater ponto'))

c = Cargo.objects.all()
cargo = []
for i in c:
    cargo.append({"content_type": "text",
                    "title": i.nome,
                    "payload": i.nome
                })
print(cargo)

print('------------------------------------------')
try:
    colaborador = Colaboradores.objects.get(email = 'kevin.hizatsuki@dmcard.com.br')
    print(colaborador)
    print(colaborador.id_role.role)
    print(colaborador.id_area.setor)
    func = Funcionalidade_Role_Areas.objects.filter(id_area=colaborador.id_area, id_role=colaborador.id_role)
    print(func)
    for i in func:
        print(i.id_funcionalidade.nome)




except ObjectDoesNotExist:
    print('fail')

print('Consulta ativo')
print(consulta_ativo(100030196033467))

print(consulta_status(100030196033467, 'Bater ponto'))

resposta = cadastro_usuario(100030196033467, 'ANALYTICS')
print('Resposta:')
print(resposta)

area = Area.objects.all()
frase = ''
lista_area = []
for i in area:

    lista_area.append({"content_type": "text",
                        "title": i.setor,
                        "payload": i.setor
                        })

print(lista_area)

usuario = Usuario.objects.get(id=100030196033467)

area = Area.objects.all()
for i in area:

    if i.setor == 'ANALYTICS':
        print('ok')
        usuario.area = i'''
'''
img = Imagem_Relatorio.objects.filter(descricao = 'Painel de bordo')

img = img.aggregate(Max('data'))['data__max']

img2 = Imagem_Relatorio.objects.filter(data = img)

print('------------Agregação max data------------')
img2 = Imagem_Relatorio.objects.filter(data = img)
print(img2[0].data)
print(datetime.datetime.now().date())
print('------------------------------------------')

area = Area.objects.get(setor = 'ANALYTICS')
usuarios = Usuario.objects.filter(area_id = area)
img = Imagem_Relatorio.objects.filter(descricao='Painel de bordo')
img_max = img.aggregate(Max('data'))['data__max']
relatorio = Imagem_Relatorio.objects.get(data = img_max)
for i in usuarios:
    if (i.role == Role.objects.get(role='ADMIN')):
        if(relatorio.enviado ==0):

            print('envia mensagem')


print('------------------------------------------')
print(consulta_ativo(100030196033467))
print('------------------------------------------')'''
'''
gerencia = Role.objects.get(role = 'GERENCIA')
diretor = Role.objects.get(role = 'DIRETOR')

usuario = Usuario.objects.get(id=100030196033467)
colaborador = Colaboradores.objects.get(email = usuario.email)


print(consulta_status(100030196033467, 'Minhas funções'))'''

