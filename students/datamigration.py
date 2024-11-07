import csv
from datetime import datetime
from models import user 


def import_books(request, file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user.objects.create(
            )

if __name__ == '__main__':
    csv_file_path = '__input__'
    import_books(csv_file_path)
