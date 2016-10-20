from django.contrib import admin
from .models import User, Product, Store

admin.autodiscover()

admin.site.register(User)

admin.site.register(Product)

admin.site.register(Store)
