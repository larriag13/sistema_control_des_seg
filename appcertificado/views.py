from django.shortcuts import render

# Create your views here.
def certificado_view(request):
    return render(request, 'appcertificado/certificado.html')