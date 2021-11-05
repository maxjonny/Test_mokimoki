from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from main import email, send_telegram
# Create your views here.

def index_view(request):
    if request.method == 'POST':
        massage = f'Имя заказчика: {request.POST.get("name")}, номер: {request.POST.get("phone")}'
        send_telegram(massage)
        email(massage)
        return redirect('home')
    return render(request, 'index.html')

def custom_handler404(request, exception):
    return HttpResponseNotFound('Error404<br>Ой, что то сломалось... <br> Это не ваша вина (но это не точно)')


