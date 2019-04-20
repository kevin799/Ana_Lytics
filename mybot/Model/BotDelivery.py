

class BotDelivery:
    def __init__(self,dbd_id,dbd_bot_id,dbd_bot_time,dbd_messaging_sender_id,dbd_messaging_recipient_id,
                 dbd_bot_messaging_time,dbd_bot_messaging_delivery_mids,dbd_bot_messaging_delivery_watermark,
                 dbd_bot_messaging_delivery_seg):
        self.dbd_id = dbd_id
        self.dbd_bot_id=dbd_bot_id
        self.dbd_bot_time=dbd_bot_time
        self.dbd_messaging_sender_id=dbd_messaging_sender_id
        self.dbd_messaging_recipient_id=dbd_messaging_recipient_id
        self.dbd_bot_messaging_time=dbd_bot_messaging_time
        self.dbd_bot_messaging_delivery_mids=dbd_bot_messaging_delivery_mids
        self.dbd_bot_messaging_delivery_watermark=dbd_bot_messaging_delivery_watermark
        self.dbd_bot_messaging_delivery_seg=dbd_bot_messaging_delivery_seg

    def setDbdId(self,dbd_id):
        self.dbd_id=dbd_id

    def getDbdId(self):
        return self.dbd_id

    def setDbdBotId(self,dbd_bot_id):
        self.dbd_bot_id=dbd_bot_id

    def getDbdBotId(self):
        return self.dbd_bot_id

    def setDbdBotTime(self,dbd_bot_time):
        self.dbd_bot_time=dbd_bot_time

    def getDbdBotTime(self):
        return self.dbd_bot_time

    def setDbdMessagingSenderId(self,dbd_messaging_sender_id):
        self.dbd_messaging_sender_id=dbd_messaging_sender_id

    def getDbdMessagingSenderId(self):
        return self.dbd_messaging_sender_id

    def setDbdMessagingRecipientId(self,dbd_messaging_recipient_id):
        self.dbd_messaging_recipient_id=dbd_messaging_recipient_id

    def getDbdMessagingRecipientId(self):
        return self.dbd_messaging_recipient_id

    def setDbdBotMessagingTime(self,dbd_bot_messaging_time):
        self.dbd_bot_messaging_time=dbd_bot_messaging_time

    def getDbdBotMessagingTime(self):
        return self.dbd_bot_messaging_time

    def setDbdBotMessagingDeliveryMids(self,dbd_bot_messaging_delivery_mids):
        self.dbd_bot_messaging_delivery_mids=dbd_bot_messaging_delivery_mids

    def getDbdBotMessagingDeliveryMids(self):
        return self.dbd_bot_messaging_delivery_mids

    def setDbdBotMessagingDeliveryWatermark(self,dbd_bot_messaging_delivery_watermark):
        self.dbd_bot_messaging_delivery_watermark=dbd_bot_messaging_delivery_watermark

    def getDbdBotMessagingDeliveryWatermark(self):
        return self.dbd_bot_messaging_delivery_watermark

    def setDbdBotMessagingDeliverySeg(self,dbd_bot_messaging_delivery_seg):
        self.dbd_bot_messaging_delivery_seg=dbd_bot_messaging_delivery_seg

    def getDbdBotMessagingDeliverySeg(self):
        return self.dbd_bot_messaging_delivery_seg