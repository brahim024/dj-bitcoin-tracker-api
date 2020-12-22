from celery import shared_task
from .models import Test, Prices

from celery.decorators import periodic_task
from celery.task.schedules import crontab
import requests 
@shared_task
def create_price_items(name):
    Test.objects.create(name=name)
    

@periodic_task(run_every=(crontab(minute='*/1')))
def run_create_items():
    create_price_items.delay(name='new2020')