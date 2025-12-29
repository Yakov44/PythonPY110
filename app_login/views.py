from django.contrib.auth import login, authenticate, logout, get_user
from django.shortcuts import render, redirect
from app_store.logic.control_cart import view_in_cart
from app_wishlist.logic.control_wishlist import view_in_wishlist

def login_view(request):
    if request.method == "GET":
        return render(request, "login/login.html")

    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data["username"], password=data["password"])  # Понимаем, что за пользователь перед нами
        if user:
            login(request, user)
            view_in_cart(user.username)
            view_in_wishlist(user.username)
            return redirect("/")

        return render(request, "login/login.html", context={"error": "Неверные данные"})


def logout_view(request):
    if request.method == "GET":
        logout(request)  # Функция разлогинивает пользователя
        return redirect('app_store:shop_view')