from django.shortcuts import render
from django.http import HttpResponseNotFound
# Create your views here.
def index_view(request):
    return render(request, 'index.html', context={})

def custom_handler404(request, exception):
    return HttpResponseNotFound('Error404<br>Ой, что то сломалось... <br> Это не ваша вина (но это не точно)')