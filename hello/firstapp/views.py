from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def products(request, productid):
    output = f'<h2>Продукт № {productid}</h2>'
    return HttpResponse(output)


def users(request, id, name):
    output = f'<h2>Пользователь</h2><h3>id: {id} Имя: {name}</hЗ>'
    return HttpResponse(output)


def index(request):
    somelist = [1, 2, 3, 4]
    data = {"someList": somelist}
    return render(request, 'index.html', context=data)

