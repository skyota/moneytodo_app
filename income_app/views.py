from django.shortcuts import render, redirect
from .models import Income
from accounts_app.models import CustomUser
from .forms import IncomeForm
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# 収入を追加
@login_required
def add_income(request):
  form = IncomeForm()
  params = {
    'form': form,
  }
  return render(request, 'income_app/add_income.html', params)

# 収入追加機能
@login_required
def incomeadd(request):
  if request.method == 'POST':
    task = Income()
    task.title = request.POST.get('title')
    task.date = request.POST.get('date')
    task.price = request.POST.get('price')
    task.user_id = CustomUser.objects.get(id=request.user.id)
    task.save()
  return redirect('user')

# 収入一覧
@login_required
def income(request):
  incomes = Income.objects.filter(user_id=request.user.id).order_by('-date')
  total_price = 0
  for income in incomes:
    total_price += income.price
  params = {
    'incomes': incomes,
    'total_price': total_price,
  }
  return render(request, 'income_app/income.html', params)

# 収入削除機能
@login_required
def delete_income(request, num):
  if num:
    income = Income.objects.get(pk=num)
    income.delete()
  return redirect('income')

# 収入更新機能
class IncomeUpdateView(UpdateView):
  model = Income
  fields = ['title', 'date', 'price']
  template_name_suffix = '_update_form'
  success_url = reverse_lazy('income')