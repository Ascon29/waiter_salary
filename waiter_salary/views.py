from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    sales_percent = 0.02
    if request.method == 'POST':
        name = request.POST.get('name')
        hourly_rate = int(request.POST.get('hourly_rate'))
        hours = int(request.POST.get('hours'))
        sales = int(request.POST.get('sales'))

        if sales >= 450000:
            sales_percent = 0.03
        total = round(hourly_rate * hours + sales * sales_percent)
        return HttpResponse(f'{name}, твоя зарплата в этом месяце без учета общего процента и без вычетов: {total} рублей.')
    return render(request, 'home.html')
