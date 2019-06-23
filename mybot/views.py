import random
import os, sys
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

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


def index(request):
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('bot')
    insert = ExampleModel(description="Funfou essa bagaca!!!!",description2 = 'karai man genial')
    insert.save()
    cadastro_usuario(123456789,'José','ATEU','Email@ateu.com')
    cluster.shutdown()
    return HttpResponse("Hello world")

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
        print(incoming_message)
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    # pprint(message)
                    print('message')
                    print(existecia_usuario(123456))
                    #cadastro_usuario(12345,'kevin.hizatsuki@dmcard.com.br')
                    print(existecia_usuario(message['sender']['id']))
                    cadastro_usuario(123456, 'Seu Boss')
                    print(primeiro_acesso(message['sender']['id']))

                    try:

                        if(existecia_usuario(message['sender']['id'])):
                            post_facebook_message(message['sender']['id'], message['message']['text'])

                    except:
                        print('exept')
                        return HttpResponse()
                if 'postback' in message:
                    # pprint(message)
                    print('postback')
                    try:

                        post_facebook_message(message['sender']['id'], message['postback']['payload'])
                    except:
                        return HttpResponse()
        save_conversation_flow(message['sender']['id'], str(incoming_message))
        return HttpResponse()
