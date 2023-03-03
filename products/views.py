import string
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.contrib import messages
from main.models import Product
from .models import Cart,CheckOut
import random
# Create your views here.





# class ArticleDetailView(DetailView):
#     model = Product
#     template_name = 'view-product.html'

def ArticleDetailView(request, product_id):
    product = Product.objects.get(pk=product_id)
    
    if request.method == 'POST' and product.number >= int(request.POST['count']):
        cart = Cart.objects.create(
            user=request.user,
            product=product,
            count=request.POST['count']
        )
        product.number-=int(cart.count)
        product.save()
        return redirect('basket')
    context = {
        'product': product,
        
    }
    return render(request, 'view-product.html', context=context)






def BasketView(request):
    product = Cart.objects.filter(user=request.user)
    result=product.count
    sum = 0
    for p in product:
        t = p.product.price * p.count
        sum += t
    context = {
        'product': product,
        'result':result,
        'sum':sum,
        't':t,
    }
    return render(request, 'cart.html', context=context)



def product_delete(request,product_id):
    product=Cart.objects.filter(id=product_id)
    if request.method=="POST":
        product.delete()
        messages.info(request, "Succesfully Deleted!")
        return redirect('index')
    return render(request, "product_delete.html", {'product':product})
    # else:
    #     messages.error(request, "Acces danied!")
    #     return redirect('index')
    








def function(request,part_id):
    object = Product.objects.get(id=part_id)
    object.delete()
    return render(request,'index.html')





def CheckOutView(request):
    checks = CheckOut.objects.all()
    all_REFS = []
    for i in checks:
        all_REFS.append(i.ref)
    new_REF = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    if new_REF in all_REFS:
        new_REF = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    
    product = Cart.objects.filter(user=request.user)
    result=product.count
    sum = 0
    for p in product:
        t = p.product.price * p.count
        sum += t
    
    if request.method == 'POST':
        cart = CheckOut(
            user=request.user,
            ref=new_REF,
            name=request.POST['name'],
            first_name=request.POST['first_name'],
            address=request.POST['address'],
            district=request.POST['district'],
            payment=request.POST['payment'],
            number=request.POST['number'],
            email=request.POST['email'],
            region=request.POST['region'],
            country=request.POST['country'],
            status='Pending',
            cost=sum,
        )
        cart.save()

        return redirect('index')
    context = {
        'product': product,
        'result':result,
        'sum':sum,
    }
    return render(request, 'checkout.html', context=context)





    