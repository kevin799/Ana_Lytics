# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer

from mybot.messenger_api import *
from mybot.database_access import *
from mybot.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max
import datetime
import time

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
    if(resposta ==1 or resposta == 5):
        usuario = Usuario.objects.get(id=fbid)
        fb.text_message("Prontinho! Finalizamos o seu cadastro 😊!")
        fb.text_message("Espero que possamos nos dar bem %s" %usuario.nome)
        funcionalidades_bot(fbid,'Start')
        #atualizando_status(fbid,'Bater ponto')
        return True

    if(resposta == -1):
        fb.text_message("Por favor insira um e-mail valido 😡")
        return True
    if(resposta == 2):
        fb.text_message("Como você se chama?🤔")
        return True
    if(resposta == 3):
        area = Area.objects.all()
        lista_area = []
        for i in area:
            lista_area.append({"content_type": "text",
                                "title": i.setor,
                                "payload": i.setor
                                })
        fb.quick_reply_message("Qual a sua área?",lista_area)
        #atualizando_status(fbid, 'Bater ponto')
        return True


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
        fucionalidades = Funcionalidade_Role_Areas.objects.filter(id_area=colaborador.id_area, id_role=colaborador.id_role)
        atualizando_ativo(fbid, 'Minhas funções', 1)
        for i in fucionalidades:
            frase = frase+ str(opcao)+ ' - ' + i.id_funcionalidade.nome+ '\n'
            opcao +=1
        frase = frase + str(opcao) + ' Sair\n '
        if(recevied_message == 'Start'):
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
            if(recevied_message in frase):
                gerenciador_funcoes(fbid,recevied_message,recevied_message)
            else:
                funcionalidades(fbid)

    except ObjectDoesNotExist:
        #Caso o usuario nao exista na base de colaborador, deve se entrar na excessão para que o usuario tenha acesso somente a funções básicas do bot.
        usuario = Usuario.objects.get(id=fbid)
        frase = ''
        opcao = 1
        fucionalidades = Funcionalidade_Role_Areas.objects.filter(id_area=usuario.area, id_role=usuario.role)
        atualizando_ativo(fbid, 'Minhas funções', 1)
        for i in fucionalidades:
            frase = frase + str(opcao) + ' - ' + i.id_funcionalidade.nome + '\n'
            opcao += 1
        frase = frase + str(opcao) + ' Sair\n'
        if (recevied_message == 'Start'):
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
            fb.quick_reply_message("Você quer uma explicação de como funciona as 'Minhas funções'???", qr)
            atualizando_status(fbid, 'Minhas funções', 2)
            return
        if (consulta_status(fbid, 'Minhas funções') == 2 and recevied_message.upper() == 'SIM'):
            fb.text_message("Vou te ensinar como usar as funções que te mostrei 😉")
            fb.text_message(
                "Sempre que vc digitar *Minhas funções* ou algo parecido vou sempre te dar uma lista assim:")
            fb.text_message(frase)
            frase_lista = frase.split('\n')
            for i in frase_lista:
                if "Bater ponto".upper() in i.upper():
                    numero = i[0]
            qr = [{"content_type": "text",
                   "title": str(numero),
                   "payload": str(numero)
                   }]
            fb.quick_reply_message(
                "Depois que eu te mandar a lista basta digitar o numero que indica a função... Sugiro que digite a função de 'bater ponto' ningem gosta de ficar arrumando lista de ponto neh ",
                qr)
            atualizando_status(fbid, 'Minhas funções', 1)
            return
        if (consulta_status(fbid, 'Minhas funções') == 1 and consulta_ativo(fbid) == 'Minhas funções'):
            if(recevied_message in frase):
                gerenciador_funcoes(fbid,recevied_message,recevied_message)
            else:
                funcionalidades(fbid)


def gerenciador_funcoes(fbid, nfuncao,recevied_message):
    try:
        usuario = Usuario.objects.get(id=fbid)
        colaborador = Colaboradores.objects.get(email=usuario.email)
        fucionalidades = Funcionalidade_Role_Areas.objects.filter(id_area=colaborador.id_area, id_role=colaborador.id_role)
        frase,funcao = '',''
        opcao = 1

        for i in fucionalidades:
            frase = frase+ str(opcao) + i.id_funcionalidade.nome+ '\n'
            opcao +=1
        frase_lista = frase.split('\n')
        print('------------------------------------')
        print(frase_lista)
        for i in frase_lista:
            if str(nfuncao) in i:
                funcao = i[1:]
        print('------------------------------------')
        print(funcao)
        if(funcao == 'Bater ponto'):
            if(consulta_ativo(fbid)=='Minhas funções'):
                atualizando_ativo(fbid,'Minhas funções',0)
                atualizando_ativo(fbid,'Bater ponto', 1)
                bater_ponto(fbid,'Start')
            else:
                bater_ponto(fbid,recevied_message)
        if(funcao == 'De acordo Painel de bordo'):
            envio_relatorio(fbid,recevied_message)
            print('--------entrou aq na funcao---------')
            return
        if(recevied_message == str(opcao)):
            atualizando_ativo(fbid,consulta_ativo(fbid),0)
            print('desgraca de erro')
    except ObjectDoesNotExist:
        #Entra nesta condição caso o usuario nao esteja contido na base de colaboradores.
        usuario = Usuario.objects.get(id=fbid)
        fucionalidades = Funcionalidade_Role_Areas.objects.filter(id_area=usuario.area, id_role=usuario.role)
        frase, funcao = '', ''
        opcao = 1

        for i in fucionalidades:
            frase = frase + str(opcao) + i.id_funcionalidade.nome + '\n'
            opcao += 1
        frase_lista = frase.split('\n')
        for i in frase_lista:
            if str(nfuncao) in i:
                funcao = i[1:]
        if (funcao == 'Bater ponto'):
            if (consulta_ativo(fbid) == 'Minhas funções'):
                atualizando_ativo(fbid, 'Minhas funções', 0)
                atualizando_ativo(fbid, 'Bater ponto', 1)
                bater_ponto(fbid, 'Start')
            else:
                bater_ponto(fbid, recevied_message)
        if (recevied_message == str(opcao)):
            atualizando_ativo(fbid, consulta_ativo(fbid), 0)

        return

def funcionalidades(fbid):
    fb = FbMessageApi(fbid)
    try:
        usuario = Usuario.objects.get(id=fbid)
        frase = ''
        opcao = 1
        colaborador = Colaboradores.objects.get(email=usuario.email)
        fucionalidades = Funcionalidade_Role_Areas.objects.filter(id_area=colaborador.id_area, id_role=colaborador.id_role)
        atualizando_ativo(fbid, 'Minhas funções', 1)
        for i in fucionalidades:
            frase = frase + str(opcao) + ' - ' + i.id_funcionalidade.nome + '\n'
            opcao += 1
        frase = frase + str(opcao) + ' - Sair\n '
        fb.text_message(frase)
    except ObjectDoesNotExist:
        usuario = Usuario.objects.get(id=fbid)
        fucionalidades = Funcionalidade_Role_Areas.objects.filter(id_area=usuario.area, id_role=usuario.role)
        frase = ''
        opcao = 1
        atualizando_ativo(fbid, 'Minhas funções', 1)
        for i in fucionalidades:
            frase = frase + str(opcao) + ' - ' + i.id_funcionalidade.nome + '\n'
            opcao += 1
        frase = frase + str(opcao) + ' - Sair\n '
        fb.text_message(frase)
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

    if(consulta_status(fbid, 'Bater ponto') == None and recevied_message=='Start'):
        fb.text_message("Deixo te explicar como funciona o sistema de bater ponto... todos os dias, exceto fim de semana, te aviso para bater o ponto tanto na entrada, no almoço e na saída... não se preoculpe... vou sempre te lembrar para bater o ponto ")
        fb.quick_reply_message("Mas claro que você não é obrigado a nada... Você quer que eu te avise para bater o ponto?",qr)
        #atualizando_status(fbid, 'Minhas funções', 0)
        #atualizando_ativo(fbid, consulta_ativo(fbid), 0)
        #atualizando_ativo(fbid, 'Bater ponto', 1)
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
        if(recevied_message == 'CLT-44 Hrs sem.'):
            cargo = Cargo.objects.get(nome = 'CLT-44 Hrs sem.')
            try:
                usuario_cargo = Usuario_cargo_hora.objects.get(id_usuario = usuario)


            except ObjectDoesNotExist:
                usuario_cargo = Usuario_cargo_hora(id_usuario = usuario,id_cargo = cargo)
                usuario_cargo.save()
                fb.quick_reply_message("Que horas você costuma chegar???", lista_horas)
                return
        try:
            usuario_cargo = Usuario_cargo_hora.objects.get(id_usuario=usuario)
            if (
                    usuario_cargo.hora_entrada != None and usuario_cargo.periodo_entrada != None and usuario_cargo.hora_almoco == None and recevied_message in horas_brutas):
                usuario_cargo.hora_almoco = recevied_message
                usuario_cargo.save()
                aplicando_periodo_almoco(fbid)
                atualizando_ativo(fbid, 'Bater ponto', 0)
                fb.text_message("Prontinho! Agora vou sempre te lembrar de bater o seu ponto!")
                return

            if (recevied_message in ['AM', 'PM']):
                usuario_cargo.periodo_entrada = recevied_message
                usuario_cargo.save()
                fb.quick_reply_message("Estamos quase terminando! Só me diz que horas você costuma almoçar (ou jantar)???",
                                       lista_hora_almoco(fbid))
                return

            if (recevied_message in horas_brutas):
                usuario_cargo.hora_entrada = recevied_message
                usuario_cargo.save()
                fb.quick_reply_message("Qual o perido que você entra?", [{"content_type": "text",
                                                                          "title": 'AM',
                                                                          "payload": 'AM'
                                                                          }, {"content_type": "text",
                                                                              "title": 'PM',
                                                                              "payload": 'PM'
                                                                              }])
                return
        except ObjectDoesNotExist:
            return


def lista_hora_almoco(fbid):
    try:
        horas = Lista_Horas.objects.all()
        horas_brutas = []
        usuario = Usuario.objects.get(id=fbid)
        for i in horas:
            horas_brutas.append(i.horas)
        usuario_cargo = Usuario_cargo_hora.objects.get(id_usuario=usuario)
        inicial = 0
        for i in horas_brutas:
            if i == usuario_cargo.hora_entrada:
                pos = inicial
            inicial+=1
        horas_brutas = horas_brutas+horas_brutas
        horas_trabalho = usuario_cargo.id_cargo.horas+1

        horas_disponiveis = horas_brutas[pos+1:pos+horas_trabalho+1]
        resposta = []
        for i in horas_disponiveis:
            resposta.append({"content_type": "text",
                            "title": i,
                            "payload": i
                        })

        return resposta
    except ObjectDoesNotExist:
        return


def aplicando_periodo_almoco(fbid):
    try:
        horas = Lista_Horas.objects.all()
        horas_brutas = []
        usuario = Usuario.objects.get(id=fbid)
        for i in horas:
            horas_brutas.append(i.horas)
        usuario_cargo = Usuario_cargo_hora.objects.get(id_usuario=usuario)
        inicial = 0
        for i in horas_brutas:
            if i == usuario_cargo.hora_entrada:
                pos = inicial
            inicial += 1
        horas_brutas = horas_brutas + horas_brutas
        horas_trabalho = usuario_cargo.id_cargo.horas + 1

        horas_disponiveis = horas_brutas[pos + 1:pos + horas_trabalho + 1]

        if ('12:00' not in horas_disponiveis):
            usuario_cargo.periodo_almoco = usuario_cargo.periodo_entrada
            usuario_cargo.save()
        else:
            inicial = 0
            for i in horas_disponiveis:
                if (i == usuario_cargo.hora_almoco):
                    pos_alm = inicial
                if (i == '12:00'):
                    pos12 = inicial

                inicial +=1
            if (usuario_cargo.periodo_entrada == 'AM' and pos_alm >= pos12):
                usuario_cargo.periodo_almoco = 'PM'
                usuario_cargo.save()
            else:
                if (usuario_cargo.periodo_entrada == 'AM' and pos_alm < pos12):
                    usuario_cargo.periodo_almoco = 'AM'
                    usuario_cargo.save()
            if (usuario_cargo.periodo_entrada == 'PM' and pos_alm >= pos12):
                usuario_cargo.periodo_almoco = 'AM'
                usuario_cargo.save()
            else:
                if (usuario_cargo.periodo_entrada == 'PM' and pos_alm < pos12):
                    usuario_cargo.periodo_almoco = 'PM'
                    usuario_cargo.save()

        return horas_disponiveis

    except ObjectDoesNotExist:
        return

def coleta_posicao_funcao(fbid,nome):
    try:
        usuario = Usuario.objects.get(id=fbid)
        colaborador = Colaboradores.objects.get(email=usuario.email)
        fucionalidades = Funcionalidade_Role_Areas.objects.filter(id_area=colaborador.id_area, id_role=colaborador.id_role)
        frase = ''
        opcao = 1
        funcao = None
        for i in fucionalidades:
            frase = frase + str(opcao) + i.id_funcionalidade.nome + '\n'
            opcao += 1
        frase_lista = frase.split('\n')
        for i in frase_lista:
            if str(nome) in i:
                funcao = i[0:1]
        return funcao
    except ObjectDoesNotExist:
        usuario = Usuario.objects.get(id=fbid)
        fucionalidades = Funcionalidade_Role_Areas.objects.filter(id_area=usuario.area, id_role=usuario.role)
        frase = ''
        opcao = 1
        funcao = None
        for i in fucionalidades:
            frase = frase + str(opcao) + i.id_funcionalidade.nome + '\n'
            opcao += 1
        frase_lista = frase.split('\n')
        for i in frase_lista:
            if str(nome) in i:
                funcao = i[0:1]
        return funcao
        return None

def envio_relatorio(fbid,recevied_message):
    try:
        usuario = Usuario.objects.get(id=fbid)
        if(usuario.area.setor == 'ANALYTICS' ):
            painel_de_bordo(fbid,recevied_message)
            return
    except ObjectDoesNotExist:
        return

def painel_de_bordo(fbid,recevied_message):
    fb = FbMessageApi(fbid)
    try:

        usuarios = Usuario.objects.get(id=fbid)
        img = Imagem_Relatorio.objects.filter(descricao='Painel de bordo')
        img_max = img.aggregate(Max('data'))['data__max']
        relatorio = Imagem_Relatorio.objects.get(data=img_max,descricao='Painel de bordo')

        if (usuarios.role == Role.objects.get(role='ADMIN')):

            if (relatorio.enviado == 0 and relatorio.data.date() == datetime.datetime.now().date() and recevied_message.upper() == 'TA ERRADO!ARRUMAR!'):
                fb.text_message("Vou enviar mais tarde então...")
                atualiza_status_relatorio('Painel de bordo',-1)
                atualizando_ativo(fbid, 'De acordo Painel de bordo', 0)
                atualiza_tab_conf(fbid,relatorio.id,-1)
                return

            if (relatorio.enviado == 0 and relatorio.data.date() == datetime.datetime.now().date() and recevied_message.upper() == 'PODE ENVIAR!'):
                fb.text_message("Vou esperar todos os acordos para o envio!")
                atualiza_status_relatorio('Painel de bordo', 1)
                atualizando_ativo(fbid, 'De acordo Painel de bordo', 0)
                atualiza_tab_conf(fbid, relatorio.id, 1)
                return


            if (relatorio.enviado == 0 and relatorio.data.date() == datetime.datetime.now().date() and recevied_message.upper() != 'PODE ENVIAR!' ):
                fb.text_message("Painel de bordo")
                fb.image_message("https://kevinmikio.ngrok.io/static/img/SAS.jpg")
                fb.quick_reply_message("Responda o mais rapido o possivel ", [{"content_type": "text",
                                                                          "title": 'Pode enviar!',
                                                                          "payload": 'Pode enviar!'
                                                                          }, {"content_type": "text",
                                                                              "title": 'Ta errado!Arrumar!',
                                                                              "payload": 'Ta errado!Arrumar!'
                                                                              }])
                return
            if(relatorio.enviado == 0 and relatorio.data.date() != datetime.datetime.now().date()):
                fb.text_message("Estou vendo que a ultima atualização que consta no banco é do dia %s"%img_max)
                fb.quick_reply_message("Posso descartar o seu de acordo deste dia? ", [{"content_type": "text",
                                                                               "title": 'Pode descartar!',
                                                                               "payload": 'Pode descartar!'
                                                                               }, {"content_type": "text",
                                                                                   "title": 'Não descartar!',
                                                                                   "payload": 'Não descartar!'
                                                                                   }])
                if(recevied_message.upper() == 'PODE DESCARTAR!'):
                    fb.text_message("Vou descartar então...")
                    atualizando_ativo(fbid, 'De acordo Painel de bordo', 0)
                    return
        return
    except ObjectDoesNotExist:
        return

def envio_prints_base_validacao(fbid):
    fb = FbMessageApi(fbid)
    if (consulta_confirmacao_relatorio('Painel Executivo', fbid) == 0 and consulta_confirmacao_relatorio('FPD',fbid) == 0
            and consulta_confirmacao_relatorio('PDD', fbid) == 0):
        '''if(consulta_ativo(fbid) == None):
            atualizando_ativo(fbid, 'De acordo Painel de bordo', 1)
        else:

            atualizando_ativo(fbid, 'De acordo Painel de bordo', 1)
        '''
        fb.text_message("Valide o paniel de bordo pfv...")
        if (consulta_confirmacao_relatorio('Painel Executivo', fbid) == 0):
            fb.text_message("Painel Executivo")
            fb.image_message('http://kevinmikio.ngrok.io/static/img/PainelExecutivo.png')
            atualiza_confirmacao_relatorio('Painel Executivo', fbid, 1)
        if (consulta_confirmacao_relatorio('FPD', fbid) == 0):
            fb.text_message("FPD")
            fb.image_message('http://kevinmikio.ngrok.io/static/img/FPD.png')
            atualiza_confirmacao_relatorio('FPD', fbid, 1)
        if (consulta_confirmacao_relatorio('PDD', fbid) == 0):
            fb.text_message("PDD")
            fb.image_message('http://kevinmikio.ngrok.io/static/img/Pdd.png')
            atualiza_confirmacao_relatorio('PDD', fbid, 1)
    return
#funcionalidades_bot(100030196033467,'sim')
#gerenciador_funcoes(100030196033467,2)

#bater_ponto(100030196033467,'12:00')

#gerenciador_funcoes(100030196033467,2)

