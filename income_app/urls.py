from . import views
from django.urls import path
from .views import IncomeUpdateView

urlpatterns = [
  # path('', views.user, name='user'),
  path('add_income/', views.add_income, name='add_income'),
  path('incomeadd/', views.incomeadd, name='incomeadd'),
  path('income/', views.income, name='income'),
  path('update_income/<int:pk>', IncomeUpdateView.as_view(), name='update_income'),
  path('delete_income/<int:num>', views.delete_income, name='delete_income'),
]