from django.shortcuts import render

# Create your views here.


def index(request):
    from datetime import datetime

    ahora = datetime.now()
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    datos = {
        'nombre': nombre,
        'apellido': apellido,
        'año': f'{ahora.year}',
    }
    return render(request, 'prueba/index.html', context=datos)


def base(request):
    return render(request, 'base.html')
