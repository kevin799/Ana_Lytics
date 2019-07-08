# -*- coding: utf-8 -*-
from mybot.Model.BotDelivery import BotDelivery
from datetime import datetime
'''a = BotDelivery(dbd_id='1',dbd_bot_id='2',dbd_bot_time='3',dbd_messaging_sender_id='4',
                dbd_messaging_recipient_id='5',dbd_bot_messaging_time='6',dbd_bot_messaging_delivery_mids='7',
                dbd_bot_messaging_delivery_watermark='8',dbd_bot_messaging_delivery_seg='9')'''

a = BotDelivery(1,2,3,4,5,6,7,8,9)

print("{'object': 'page', 'entry': [{'id': '1894084317375665', 'time': 1557007455810, 'messaging': [{'sender': {'id': '100030196033467', 'community': {'id': '939986719483510'}}, 'recipient': {'id': '1894084317375665'}, 'timestamp': 1557007455401, 'read': {'watermark': 1557007454144, 'seq': 0}}]}]}".replace("'",'"'))





