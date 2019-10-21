# -*- coding: utf-8 -*-
import random
import os, sys

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render

from Ana_Lytics import settings
from mybot.funcoes_bot import *
from mybot.model_cmd import *
from mybot.messenger_api import *
from mybot.fb_setting import *

from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster
from mybot.models import ExampleModel
from django.http import HttpResponse
from mybot.database_access import *
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from mybot.Area_teste.Teste import *
'''
def post_facebook_message(fbid, recevied_message):
    # user_details_url = "https://graph.facebook.com/v2.6/%s" % fbid
    # user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': PAGE_ACCESS_TOKEN}
    # user_details = requests.get(user_details_url, user_details_params).json()

    fb = FbMessageApi(fbid)
    if recevied_message == "teste":
        fb.text_message("deu bom")
        return 0
'''
chatterbot = ChatBot('Ana Lytics',read_only=True,
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ])
treinar(chatterbot)

def index(request):
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('bot')
    insert = ExampleModel(description="Funfou essa bagaca!!!!",description2 = 'karai man genial')
    insert.save()
    cadastro_usuario_cassandra(123456789,'José','ATEU','Email@ateu.com')
    cluster.shutdown()
    return HttpResponse("Hello world")

def bot_on(request):
    return render(request, "mybot/index.html")

def imagem(request):
    return render(request, "mybot/image.html")

def acao_inter(request):
    return render(request, "mybot/acaoInter.html")

def sas_print(request):
    return render(request,"mybot/painelBordo.html")

def painelExecutivo_print(request):
    return render(request,"mybot/painelExecutivo.html")

def pdd_print(request):
    return render(request,"mybot/pdd.html")

def fpd_print(request):
    return render(request,"mybot/fpd.html")

def ipf_print(request):
    return render(request,"mybot/ipf.html")



class MyBotView(generic.View):


    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))

        #print(incoming_message)
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    print(message)
                    print('message')

                    #cadastro_usuario(12345,'kevin.hizatsuki@dmcard.com.br')


                    '''!!!!!!!!!!!!!  VOLTAR TRY PELO AMOR DE DEUS   !!!!!!!!!'''
                    try:
                        fb = FbMessageApi(message['sender']['id'])
                        if(existecia_usuario(message['sender']['id'])):
                            if (terminou_cadastro(message['sender']['id'])):
                                cadastro(message['sender']['id'], message['message']['text'])
                                return HttpResponse()
                            if (message['message']['text']=="funcionalidade" or consulta_ativo(message['sender']['id'])=='Minhas funções'):
                                print('entrou funcionalidade')
                                funcionalidades_bot(message['sender']['id'],message['message']['text'])
                                return HttpResponse()
                            if (consulta_ativo(message['sender']['id'])!= None):
                                print('chamou gerenciador de funcao na view')
                                gerenciador_funcoes(message['sender']['id'],coleta_posicao_funcao(message['sender']['id'],consulta_ativo(message['sender']['id'])),message['message']['text'])
                                break
                                return HttpResponse()
                            if(message['message']['text'] == 'minhas funcoes'):
                                print('entrou')
                                gerenciador_funcoes(message['sender']['id'],consulta_funcionalidade('Minhas funções'),message['message']['text'])
                                break
                                return HttpResponse()
                            response = chatterbot.get_response(message['message']['text'])
                            print(float(response.confidence)*0.01)
                            if float(response.confidence)>0.5:
                                fb.text_message(str(response))
                            else:
                                fb.text_message('Nao sei ainda o que responder :(')


                    except Exception as e:
                        print(e)
                        return HttpResponse()
                if 'postback' in message:
                    # pprint(message)
                    print('postback')
                    try:
                        print('ok')
                        cadastro(message['sender']['id'], message['postback']['payload'])
                    except:
                        return HttpResponse()
        save_conversation_flow(message['sender']['id'], str(incoming_message))
        return HttpResponse()
