from django.shortcuts import render
from .models import Product
from django.views import View
# Create your views here.




class IndexView(View):
    def get(self,request, ):
        products=Product.objects.all()
        return render(request, 'index.html',{'products':products})
    