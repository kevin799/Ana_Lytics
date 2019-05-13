from mybot.messenger_api import *


def post_facebook_message(fbid, recevied_message):
    # user_details_url = "https://graph.facebook.com/v2.6/%s" % fbid
    # user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': PAGE_ACCESS_TOKEN}
    # user_details = requests.get(user_details_url, user_details_params).json()
    fb = FbMessageApi(fbid)
    if recevied_message == "teste":
        fb.text_message("deu bom")
        return 0

