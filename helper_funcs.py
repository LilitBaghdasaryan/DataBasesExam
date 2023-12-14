from random import randrange
from datetime import datetime, timedelta
from datetime import date
from json import JSONEncoder

def random_date():
    start = datetime.strptime('1/1/1974', '%m/%d/%Y')
    end = datetime.strptime('1/1/2024', '%m/%d/%Y')
    delta = end - start
    random_days = randrange(delta.days)
    return (start + timedelta(days=random_days)).date()

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)
