from django.contrib import admin
from django.urls import path, include
from core.views import PessoaViewSet
from rest_framework import routers




router = routers.DefaultRouter()
router.register(r'pessoa',PessoaViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
