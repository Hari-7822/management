import csv
from datetime import datetime
from models import user 


def DataMigrate(request, file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user.objects.create()   


class Logs:
    def Db(self, info):
        pass
    
    def time(self, info):
        pass
    
    def events(self, req, info):
        pass