from django.contrib import admin
from django.urls import path
from core.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name='homepage'),
    path('delete/<int:id>/',delete,name='delete'),
    path('all/',deleteall,name='all'),
    path('update/<int:id>/',update,name='update')
]
