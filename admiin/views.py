from django.shortcuts import render,redirect
from products.models import CheckOut,Cart
from .forms import NewProductForm,ProductForm
from django.contrib import messages
from main.models import Product
from django.shortcuts import get_object_or_404
# Create your views here.



# def AddProductView(request):
#     return render(request,'admin/add-product.html')




def AddProductView(request):
    if request.method=="GET":
        form=NewProductForm()
        return render(request, 'admiin/add-product.html',{'form':form})
    
    elif request.method == "POST":
        form =NewProductForm(data=request.POST,files=request.FILES)    # "data=request.POST"  malumotlarimizni oladi'   "files=request.FILES"    Rasmlarimizni oladi
        if form.is_valid():
            form.save(request)
     
            messages.success(request, "Succesfully Created")
            return redirect('index')
        return render(request, 'admiin/add-product.html',{'form':form})
    




def OrderView(request,user_id):
    order=Cart.objects.filter(is_superuser=request.user)
    orders=get_object_or_404(CheckOut,id=user_id)
    sum = 0
    for p in order:
        sum += p.count
    context={
        'orders':orders,
        'order':order,
        'sum':sum,
    }
    return render(request, 'admiin/view-order.html',context=context)






def AdminIndexView(request):
    products=Product.objects.all()
    orders=CheckOut.objects.all()
    context={
        'products':products,
        'orders':orders
    }
    return render(request, 'admiin/index.html',context=context)






def product_update(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    if request.user.is_superuser:
        if request.method=="GET":
            form=ProductForm(instance=product)
            return render(request, 'admiin/product_update.html',{'form':form, 'pr':product})
        elif request.method=="POST":
            form=ProductForm(instance=product,data=request.POST,files=request.FILES)
            if form.is_valid():
                form.save()
                # if request.FILES.getlist('images'):
                #     ProductImage.objects.filter(product=product).delete()
                #     for i in request.FILES.getlist("images"):
                #         ProductImage.objects.create(product=product,image=i)
                messages.success(request, "Succesfully Updated!")
                return redirect('detail',product.id)
            return render(request, 'admiin/product_update.html',{'form':form, 'pr':product})
    else:
        messages.error(request, "Acces danied!")
        return redirect('index')
    

# def delete(request,product_id):
    # product=get_object_or_404(Product,id=product_id)
    # if request.user.is_superuser:
    #     product.delete()
    #     messages.info(request, "Succesfully Deleted!")
    #     return redirect('aindex')
    # # else:
    # #     messages.error(request, "Acces danied!")
    # #     return redirect('index')
    # return render(request, "admiin/product_delete.html")




def delete(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    if request.method=="POST":
        product.delete()
        messages.info(request, "Succesfully Deleted!")
        return redirect('index')
    return render(request, "admiin/product_delete.html", {'product':product})
    