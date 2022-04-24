from django.shortcuts import render
from django.shortcuts import redirect , render
from django.contrib.auth import authenticate , login
from django.views.generic import View
from .forms import User

# Create your views here.

class UserFormView(View):
    form_class = User

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #creats object from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username = username , password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return # uuid