from .models import Category
from assign.models import social as social_model
from assign.models import about_us as about_us_model


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_about_us(request):
    about_us = about_us_model.objects.first()  # Get the first instance of about_us
    return dict(about_us=about_us)

def get_social(request):
    social = social_model.objects.all()  # Get all instances of social
    return dict(social=social)