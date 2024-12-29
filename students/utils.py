import csv
from datetime import datetime

from django.contrib import messages

from models import user 


def DataMigrate(request, file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user.objects.create()   


def FieldFetch(request, form, model, *args, **kwargs):
    if request.method == "POST":
        pass
    else:
        return messages.add_message(Warning, f"Inavlid method {request.method}")


class Logs:
    def Db(self, info):
        pass
    
    def time(self, info):
        pass
    
    def events(self, req, info):
        pass


