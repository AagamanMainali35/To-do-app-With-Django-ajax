from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name='homepage'),
    path('api/delete/<int:id>/', delete),
    path('api/delete/', deleteall), 
    path('api/update/<int:id>/', update, name='update'),
    path('api/get/', getData, name='apiforgettingdata'),
    path('api/get/<int:id>/', getSingleData, name='api_get_single_data'),
    path('api/create/', createdata, name='createdata'),
]
