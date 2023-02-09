import pytz
from datetime import datetime

def get_current_time():
    tz = pytz.timezone('America/Sao_Paulo')
    return datetime.now(tz)

def get_current_timestamp( isInt = False):
    d = datetime.timestamp( get_current_time() )
    return d if not isInt else int(round(d,0))
    
if __name__ == '__main__':
    print(get_current_time())
    print( get_current_timestamp(False) )