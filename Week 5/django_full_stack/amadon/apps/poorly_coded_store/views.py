from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    product_id = float(request.POST.get("price"))
    selected_product = Product.objects.get(id=product_id)
    request.session["price_from_form"] = float(selected_product.price)
    request.session['quantity_from_form'] = int(request.POST.get("quantity"))
    request.session["total_charge"] = request.session["quantity_from_form"] * request.session["price_from_form"]
    # print(request.session["price_from_form"])
    # print(request.session["quantity_from_form"])
    # print(request.session["total_charge"])
    order = Order.objects.create(quantity_ordered=request.session['quantity_from_form'], total_price=request.session["total_charge"])
    order.save()
    return redirect('/success')

def success(request):
    all_orders = Order.objects.all()
    total = 0
    total_quantity = 0
    last_order = Order.objects.last()
    for order in all_orders:
        total += order.total_price
        total_quantity += order.quantity_ordered
    print(total_quantity)
    print(last_order.quantity_ordered)
    print(all_orders)
    context = {
        'orders' : all_orders,
        'total_p' : total,
        "last" : last_order,
        "quant" : total_quantity
    }
    return render(request, "store/checkout.html", context)