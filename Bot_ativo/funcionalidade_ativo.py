# -*- coding: utf-8 -*-
from funcao_acesso import *
from datetime import datetime

def bater_ponto(fbid):
    fb = FbMessageApi(fbid)
    fb.text_message("Oieee!!! Não esquece de bater o ponto :)!")

def ida_almoco(fbid):
    fb = FbMessageApi(fbid)
    fb.text_message("Chegou a hora boa!!! Bora encher o buxo!!! AH! Não esquece de bater o ponto ok!")

def volta_almoco(fbid):
    fb = FbMessageApi(fbid)
    fb.text_message("É triste te trazer essa notícia... mas acabou o intervalo 😭... Mas nâo esquece de bater o ponto...")

def envia_painel_de_bordo(fbid):
    fb = FbMessageApi(fbid)


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
        if (consulta_confirmacao_relatorio('IPF', fbid) == 0):
            fb.text_message("IPF")
            fb.image_message('http://kevinmikio.ngrok.io/static/img/Ipf.png')
            atualiza_confirmacao_relatorio('IPF', fbid, 1)
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

def envio_geral(fbid):
    fb = FbMessageApi(fbid)
    fb.text_message("Segue o Painel de bordo atualizado")
    fb.image_message("https://kevinmikio.ngrok.io/static/img/SAS.jpg")
    return

def lembrete_admin(fbid):
    fb = FbMessageApi(fbid)
    fb.text_message("Relatorio enviado para os demais colaboradores.")

def lembrete_erro(fbid):
    fb = FbMessageApi(fbid)
    fb.text_message("Foi constatado um erro no ultimo envio, valide com a novos prints.")


def comunicado_geral(fbid):
    fb = FbMessageApi(fbid)
    fb.text_message(mensagem_comunicado_geral())

