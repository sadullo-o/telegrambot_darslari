import requests
from bs4 import BeautifulSoup


def get_info(viloyat):

    manzil = f'https://namozvaqti.uz/ramazon/{viloyat}'

    r = requests.get(manzil)

    matn = BeautifulSoup(r.text, 'html.parser')

    matn = matn.find(class_='table_calendar').text
    w = matn.split('\n\n')
    yangi = []
    for i in w:
        yangi.append(i.replace('\n', '  -  '))
    return yangi
