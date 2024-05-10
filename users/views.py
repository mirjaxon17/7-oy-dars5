
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from category.models import Category,Products
from django.contrib.auth.mixins import LoginRequiredMixin
#from .models import User
from .forms import UserLoginForm,UserRegisterForm

class LandingPageView(View):
    def get(self, request):
        category = Category.objects.all()
        product = Products.objects.all()
        users = User.objects.all()
        contex = {
            'category':category,
            'product':product,
            'users':users

        }
        return render(request, 'main/index.html',contex)

class UserRegisterView(View):
    def get(self, request):
        return render(request, "auth/register.html")

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password_1 = request.POST["password_1"]
        password_2 = request.POST["password_2"]
        if password_1 == password_2:
            user_check = User.objects.filter(username=username, password=password_1)
            if user_check:
                return render(request, "auth/register.html")
            else:
                user = User(first_name=first_name, last_name=last_name, email=email, username=username)
                user.set_password(password_1)
                user.save()
                return redirect("login")
        else:
            return render(request, "auth/register.html")


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {
            "form": form
        }
        return render(request, "auth/login.html", context)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        data = {
            "username": username,
            "password": password
        }
        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("landing")

        else:
            form = UserLoginForm()
            context = {
                "form": form
            }
            return render(request, "auth/login.html", context)

class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("landing")