# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer

from mybot.messenger_api import *
from mybot.database_access import *
from mybot.models import *
from django.core.exceptions import ObjectDoesNotExist


def cadastro(fbid, recevied_message):
    # user_details_url = "https://graph.facebook.com/v2.6/%s" % fbid
    # user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': PAGE_ACCESS_TOKEN}
    # user_details = requests.get(user_details_url, user_details_params).json()
    fb = FbMessageApi(fbid)

    if(primeiro_acesso(fbid)):
        fb.text_message("Pera... eu ainda nao te conheço 😱😱😱🤔")
        qr = [ {"content_type": "text",
                "title": "Sim",
                "payload": "Sim"
                },
                {"content_type": "text",
                "title": "Não",
                "payload": "Não"
                }]

        fb.quick_reply_message("Que tal começarmos o seu cadastro agora 🤔???",qr)
        return True

    try:
        print('Entrou antes do acesso')
        usuario = Usuario.objects.get(id=fbid)
        print('entrou depois')
    except ObjectDoesNotExist:
        return True
    if(usuario.status_acesso==0 and recevied_message.upper() == 'SIM'):
        usuario.status_acesso=1
        usuario.save()
        fb.text_message("Tudo bem... Me passa o seu e-mail pfv")
        return True
    if(usuario.status_acesso==0 and recevied_message.upper() == 'NÃO'):
        fb.text_message("Tudo bem 😭... Mais tarde eu te conheço melhor ")
        return True
    if (usuario.status_acesso == 0):
        fb.text_message("Pera... eu ainda nao te conheço 😱😱😱🤔")
        qr = [{"content_type": "text",
               "title": "Sim",
               "payload": "Sim"
               },
              {"content_type": "text",
               "title": "Não",
               "payload": "Não"
               }]

        fb.quick_reply_message("Que tal começarmos o seu cadastro agora 🤔???", qr)
        return True
    resposta = cadastro_usuario(fbid, recevied_message)
    if(resposta ==1 or resposta == 3):
        usuario = Usuario.objects.get(id=fbid)
        fb.text_message("Prontinho! Finalizamos o seu cadastro 😊!")
        fb.text_message("Espero que possamos nos dar bem %s" %usuario.nome)
        atualizando_status(fbid,'Bater ponto')
        return True

    if(resposta == -1):
        fb.text_message("Por favor insira um e-mail valido 😡")
        return True
    if(resposta == 2):
        fb.text_message("Como você se chama?🤔")
        return True
    if(resposta==4):
        fb.text_message("Pode comemorar meu caro xovi")
        atualizando_status(fbid, 'Bater ponto')
        return False

def bater_ponto(fbid, recevied_message):

    return

def treinar(chatterbot):
    lista_dialogo = []
    trainer = ListTrainer(chatterbot)
    conversa = Conversa_ML.objects.values('conversa')
    for i in conversa:
        lista_dialogo.append(i['conversa'])
    trainer.train(lista_dialogo)
    print(lista_dialogo)