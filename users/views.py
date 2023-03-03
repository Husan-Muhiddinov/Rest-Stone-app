from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SignupForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.


class SignupView(View):
    def get(self,request):
        return render(request, 'registration/signup.html',{'form':SignupForm()})
    


    def post(self,request):
        form=SignupForm(data=request.POST)    # inputlarga kiritilgan malumotlarni olish 
        if form.is_valid():   # formamiz yaroqli bo'lsa biz buni saqlaymiz
            form.save()
            messages.success(request, "Your account is succesfully created.")
            return redirect('login')
        return render(request, 'registration/signup.html', {'form':form})   # agar ro'yhatdan o'tish valid bo'lsa xatolikni ko'rsatib beradi
    

    def test_func(self):
        user=self.request.user
        if user.is_authenticated:
            return False
        return True