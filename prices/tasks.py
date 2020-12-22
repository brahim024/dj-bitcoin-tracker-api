from celery import shared_task
from .models import Prices


@shared_task
def create_price_project(name,image,price,cap_rank,market_cap):
    Price.objects.create(name=name)
    Price.objects.create(image=image)
    Price.objects.create(price=price)
    Price.objects.create(market_cap=market_cap)
    