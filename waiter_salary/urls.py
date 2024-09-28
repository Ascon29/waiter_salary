from django.urls import path
from waiter_salary.views import home
from waiter_salary.apps import WaiterSalaryConfig

app_name = WaiterSalaryConfig.name

urlpatterns = [
    path('', home, name='home'),
]