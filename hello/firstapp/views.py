from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Order
from .forms import UserForm


# Create your views here.
def products(request, productid):
    output = f'<h2>Продукт № {productid}</h2>'
    return HttpResponse(output)


def users(request, id, name):
    output = f'<h2>Пользователь</h2><h3>id: {id} Имя: {name}</hЗ>'
    return HttpResponse(output)


def index(request):
    object_list = Order.objects.all()
    data = {"object_list": object_list}
    return render(request, 'index.html', context=data)


def GreateForm(request):

    if request.method == "POST":

        form = UserForm(request.POST)
        name = request.POST.get('name')
        age = request.POST.get('age')
        if form.is_valid():
            Order.objects.create(order_name=name, order_phone=age)
            return HttpResponseRedirect("/")
        else:
            return HttpResponse(f'{name}{age} not OK')
    else:
        form = UserForm()
        object_list = Order.objects.all()
        print(object_list)
        data = {"object_list": object_list, "form": form}
        return render(request, 'greate.html', context=data, )

def edit(request):
    pass




def delete(request,id):
    pers = Order.objects.get(id=id)
    try:
        pers.delete()
        return HttpResponseRedirect("/")
    except pers.DoesNotExit:
        return HttpResponseNotFound("<h2> No Client found </h2>")

