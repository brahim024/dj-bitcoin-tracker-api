from celery import shared_task
from .models import Prices
from celery.decorators import periodic_task
#from celery.tasks.schedules import crontab
@shared_task
def create_price_items(name,image,price,cap_rank,market_cap):
    Price.objects.create(name=name)
    Price.objects.create(image=image)
    Price.objects.create(price=price)
    Price.objects.create(market_cap=market_cap)
#@periodic_task(run_every=(crontab(minute='*/1')))
#def run_create_items():
#    create_price_items.delay(name='new2020')