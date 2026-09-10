from django.urls import path
from . import views

app_name='appcertificado'

urlpatterns = [
    path('certificado/', views.certificado_view,name='certificado'),
]
