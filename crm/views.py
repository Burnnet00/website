from django.shortcuts import render
from .models import Orders
from .forms import OrdersForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable

def index(request):
    orders = Orders.objects.all()
    slider = CmsSlider.objects.all()
    form = OrdersForm#передаємо створений клас форм
    pk1 = PriceCard.objects.get(pk=1)
    pk2 = PriceCard.objects.get(pk=2)
    price_t = PriceTable.objects.all()
    dict_ob = {
        'orders': orders,
        'form': form,
        'slider': slider,
        'pk1': pk1,
        'pk2': pk2,
        'price_t': price_t
    }
    return render(request, "./index.html", dict_ob)
def thx(request):
    if request.POST:
        name = request.POST['name']#отримуемо параметри з полями name, phone
        phone = request.POST['phone']
        element = Orders(o_name=name, o_phone=phone)#створюємо новий екземпляр класу Ордерс, присвоюємо поля
        element.save()#зберігаємо методом сейв
        return render(request, 'thx.html', {
            'name': name,
            'phone': phone,
        })#передаємо словник ключі:значення створених зміних (функція обробки htmlформ та збереження в бд)
    else:
        return render(request, 'thx.html')