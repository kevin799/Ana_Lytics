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
        #atualizando_status(fbid,'Bater ponto')
        return True

    if(resposta == -1):
        fb.text_message("Por favor insira um e-mail valido 😡")
        return True
    if(resposta == 2):
        fb.text_message("Como você se chama?🤔")
        return True
    if(resposta==4):
        fb.text_message("Pode comemorar meu caro xovi")
        #atualizando_status(fbid, 'Bater ponto')
        return False



def treinar(chatterbot):
    lista_dialogo = []
    trainer = ListTrainer(chatterbot)
    conversa = Conversa_ML.objects.values('conversa')
    for i in conversa:
        lista_dialogo.append(i['conversa'])
    trainer.train(lista_dialogo)
    print(lista_dialogo)


def funcionalidades_bot(fbid, recevied_message):

    fb = FbMessageApi(fbid)
    try:
        usuario = Usuario.objects.get(id=fbid)
        frase = ''
        opcao = 1
        colaborador = Colaboradores.objects.get(email = usuario.email)
        fucionalidades = Funcionalidades_bot.objects.filter(status=1,role = colaborador.id_role)
        atualizando_ativo(fbid, 'Minhas funções', 1)
        for i in fucionalidades:
            frase = frase+ str(opcao)+ ' - ' + i.nome+ '\n'
            opcao +=1
        frase = frase + str(opcao+1) + ' Sair\n '
        if(consulta_status(fbid,'Minhas funções')==None):
            fb.text_message("Sabe... Mesmo sendo um robô 🤖  sei fazer algumas coisas ...")
            fb.text_message("Oha o que estou habilitado a fazer para vc 😎")
            fb.text_message(frase)
            qr = [{"content_type": "text",
                   "title": "Sim",
                   "payload": "Sim"
                   },
                  {"content_type": "text",
                   "title": "Não",
                   "payload": "Não"
                   }]
            fb.quick_reply_message("Você quer uma explicação de como funciona as 'Minhas funções'???",qr)
            atualizando_status(fbid, 'Minhas funções',2)
            return
        if(consulta_status(fbid,'Minhas funções')==2 and recevied_message.upper() == 'SIM'):
            fb.text_message("Vou te ensinar como usar as funções que te mostrei 😉")
            fb.text_message("Sempre que vc digitar *Minhas funções* ou algo parecido vou sempre te dar uma lista assim:")
            fb.text_message(frase)
            frase_lista = frase.split('\n')
            for i in frase_lista:
                if "Bater ponto".upper() in i.upper():
                    numero = i[0]
            qr = [{"content_type": "text",
                   "title": str(numero),
                   "payload": str(numero)
                   }]
            fb.quick_reply_message("Depois que eu te mandar a lista basta digitar o numero que indica a função... Sugiro que digite a função de 'bater ponto' ningem gosta de ficar arrumando lista de ponto neh ",qr)
            atualizando_status(fbid, 'Minhas funções', 1)
            return
        if (consulta_status(fbid, 'Minhas funções') == 1 and consulta_ativo(fbid) == 'Minhas funções'):
            gerenciador_funcoes(fbid,recevied_message)

    except ObjectDoesNotExist:
        #Caso o usuario nao exista na base de colaborador, deve se entrar na excessão para que o usuario tenha acesso somente a funções básicas do bot.
        fucionalidades = Funcionalidades_bot.objects.filter(status=1, role=1)
        for i in fucionalidades:
            frase = frase + i.nome+ '\n'
        print('nao existe')


def gerenciador_funcoes(fbid, nfuncao):
    try:
        usuario = Usuario.objects.get(id=fbid)
        colaborador = Colaboradores.objects.get(email=usuario.email)
        fucionalidades = Funcionalidades_bot.objects.filter(status=1, role=colaborador.id_role)
        frase = ''
        opcao = 1

        for i in fucionalidades:
            frase = frase+ str(opcao) + i.nome+ '\n'
            opcao +=1
        frase_lista = frase.split('\n')
        for i in frase_lista:
            if str(nfuncao) in i:
                funcao = i[1:]
        if(funcao == 'Bater ponto'):
            bater_ponto(fbid,'start')

    except ObjectDoesNotExist:
        return


def bater_ponto(fbid, recevied_message):
    fb = FbMessageApi(fbid)

    qr = [{"content_type": "text",
           "title": "Sim",
           "payload": "Sim"
           },
          {"content_type": "text",
           "title": "Não",
           "payload": "Não"
           }]
    if (recevied_message.upper() == 'SIM' and consulta_status(fbid, 'Bater ponto') == None and consulta_ativo(fbid) == 'Bater ponto'):
        cargo = []
        c = Cargo.objects.all()
        for i in c:
            cargo.append({"content_type": "text",
                            "title": i.nome,
                            "payload": i.nome
                        })
        fb.quick_reply_message("Me fala qual a sua posição na DM???",cargo)
        atualizando_status(fbid, 'Bater ponto', 1)
        return

    if(consulta_status(fbid, 'Bater ponto') == None):
        fb.text_message("Deixo te explicar como funciona o sistema de bater ponto... todos os dias, exceto fim de semana, te aviso para bater o ponto tanto na entrada, no almoço e na saída... não se preoculpe... vou sempre te lembrar para bater o ponto ")
        fb.quick_reply_message("Mas claro que você não é obrigado a nada... Você quer que eu te avise para bater o ponto?",qr)
        atualizando_status(fbid, 'Minhas funções', 0)
        atualizando_ativo(fbid, consulta_ativo(fbid), 0)
        atualizando_ativo(fbid, 'Bater ponto', 1)
        return
    if(recevied_message.upper()== 'NÂO'):
        fb.text_message("Tudo bem... quando você quiser ativar a função basta digitar 'Minhas funções'")
        atualizando_ativo(fbid, 'Bater ponto', 0)
        atualizando_status(fbid, 'Bater ponto', 0)
        return
    if(consulta_ativo(fbid) == 'Bater ponto'):
        lista_horas = []
        horas = Lista_Horas.objects.all()
        horas_brutas = []
        usuario = Usuario.objects.get(id=fbid)
        for i in horas:
            horas_brutas.append(i.horas)
            lista_horas.append({"content_type": "text",
                            "title": i.horas,
                            "payload": i.horas
                        })
        if(recevied_message == 'CLT - 44 Hrs semanais'):
            cargo = Cargo.objects.get(nome = 'CLT - 44 Hrs semanais')
            try:
                usuario_cargo = Usuario_cargo_hora.objects.get(id_usuario = usuario)
                print('aaaaaaaaaaaaaaaaaaaaaaaaaaa')
                return
            except ObjectDoesNotExist:
                print('bbbbbbbbbbbbbbbbbbbbbbbbbbb')
                usuario_cargo = Usuario_cargo_hora(id_usuario = usuario,id_cargo = cargo)
                usuario_cargo.save()
                fb.quick_reply_message("Que horas você costuma chegar???", lista_horas)
                return
        if (recevied_message in horas_brutas):
            usuario_cargo = Usuario_cargo_hora.objects.get(id_usuario = fbid)
            usuario_cargo.hora_entrada = recevied_message
            usuario_cargo.save()
            return




#funcionalidades_bot(100030196033467,'sim')
#gerenciador_funcoes(100030196033467,2)

bater_ponto(100030196033467,'CLT - 44 Hrs semanais')

