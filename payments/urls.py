from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('process/<int:order_id>/', views.payment_process, name='process'),
    path('done/<int:order_id>/', views.payment_done, name='done'),
    path('cancelled/', views.payment_cancelled, name='cancelled'),
]
