from django.shortcuts import render
from random import choice

def home(request):
    return render(request, "home.html")

def result(request):
    if request.GET.get("length"):
        text = "abcdefghijklmnopqrstuvwxyz"
        if request.GET.get("uc"):
            text += text.upper()
        if request.GET.get("di"):
            text += "0123456789"
        le = int(request.GET.get("length"))
        pw = "".join(choice(text) for _ in range(le))
        return render(request, "result.html", {"msg": pw})
    else:
        return render(request, "result.html")

def page404(request, exception):
    return render(request, "page404.html", status=404)
