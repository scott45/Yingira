from django.conf.urls import patterns, include, url
from django.contrib import admin

from enter import views

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.home, name='home'),
                       url(r'^index/$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^add_product/$', views.add_product, name='add_product'),
                       url(r'^add_store/$', views.add_store, name='add_store'),
                       url(r'^product/$', views.product, name='product'),
                       url(r'^store/$', views.store, name='store'),
                       url(r'^register/$', views.register, name='register'),
                       )
