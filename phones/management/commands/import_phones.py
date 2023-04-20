import csv

from phones.models import Phone
from django.template.defaultfilters import slugify


class Phone_csv():
    def handle(self, *args, **options):
        # with open('C:\\Users\\ayuro\\Desktop\\ALL\HW\\django\\work_with_database\\phones\\management\\commands\\phones.csv', 'r') as file:
        with open('phones\\management\\commands\\phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for items in phones:
            brand = Phone(
                name=items['name'],
                price=items['price'],
                image=items['image'],
                release_date=items['release_date'],
                lte_exists=items['lte_exists'],
                slug=slugify(items['name']))
            brand.save()





