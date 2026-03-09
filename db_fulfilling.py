import json
import os
import django


# Установка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'univer_easy_conf.settings')
django.setup()

# Теперь можно импортировать модели
from UniverEasy.models import Univer, Faculty

DB_NAME = "univer_easy_db"
DB_USER = "uni"
DB_PASSWORD = "test"
DB_HOST = "localhost"
DB_PORT = "5432"

JSON_FILE = 'db_data.json'

with open(JSON_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

def to_slug(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError('STR ONLY')
    lat = [
            'a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k',
            'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 'c',
            'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya'
          ]
    start_ind = ord('а')
    res = ''
    for i in text.lower():
        if 'а' <= i <='я':
            res += lat[ord(i) - start_ind]
        elif i == 'ё':
            res += 'yo'
        elif i == ' ':
            res += '-'
        else:
            res += i
    return res

def fill_unik(all_data):
    un_data = all_data['UniverEasy_univer']

    for u in un_data:
        Univer.objects.create(**u)


    series_uniks = Univer.objects.all()


    Univer.objects.bulk_update(series_uniks, ['id', 'name', 'slug'])


def fill_facs(all_data):
    facs_data = all_data['UniverEasy_faculty']

    for f in facs_data:
        Faculty.objects.create(**f)

    series_facs = Faculty.objects.all()
    Faculty.objects.bulk_update(series_facs, ['name', 'slug', 'univer_id'])

#fill_unik(data)
fill_facs(data)




