# -*- coding: utf-8 -*-
from funcao_acesso import *
from messenger_api import *
from funcionalidade_ativo import *


'''for i in get_list_user():
    envio_ola(i)'''

for i in ponto_entrada():
    bater_ponto(i)

for i in ponto_ida_almoco():
    ida_almoco(i)

for i in ponto_volta_almoco():
    volta_almoco(i)


if(confirmacao_de_todos_os_admins()):
    for i in retorna_basic_analytics():
        envio_geral(i)
    for i in retorna_admins_analytics():
        lembrete_admin(i)
    update_relatorio_imagem()