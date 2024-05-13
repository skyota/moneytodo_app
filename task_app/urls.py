from . import views
from django.urls import path
from .views import PaymentUpdateView, TaskUpdateView, WeekCalendar

urlpatterns = [
  path('', WeekCalendar.as_view(), name='user'),
  path('<int:year>/<int:month>/<int:day>/', WeekCalendar.as_view(), name='user'),
  path('add_task/', views.add_task, name='add_task'),
  path('add_payment/', views.add_payment, name='add_payment'),
  path('add/', views.add, name='add'),
  path('payment/', views.payment, name='payment'),
  path('update_payment/<int:pk>', PaymentUpdateView.as_view(), name='update_payment'),
  path('delete_payment/<int:num>', views.delete_payment, name='delete_payment'),
  path('task/', views.task, name='task'),
  path('update_task/<int:pk>', TaskUpdateView.as_view(), name='update_task'),
  path('delete_task/<int:num>', views.delete_task, name='delete_task'),
]