from datetime import datetime
import pytz

utcmoment_naive = datetime.utcnow()
utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)


try:
    localDatetime = utcmoment.astimezone(pytz.timezone('America/Sao_Paulo'))

    print(localDatetime.strftime('%H:00'))
except pytz.exceptions.NonExistentTimeError as e:
    print("NonExistentTimeError")