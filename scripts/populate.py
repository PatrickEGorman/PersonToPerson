import django
import os

django.setup()

from apps.PostingOrganizer.models import Category

Category.objects.all().delete()

os.system('python Categories/set_default_categories.py')
