import datetime
from django.shortcuts import render, redirect
from .models import Task
from accounts_app.models import CustomUser
from .forms import MoneyTaskForm
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .mixins import WeekWithScheduleMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

# タスクを追加
@login_required
def add_task(request):
  form = MoneyTaskForm()
  params = {
    'form': form,
  }
  return render(request, 'task_app/add_task.html', params)

# 支出を追加
@login_required
def add_payment(request):
  return render(request, 'task_app/add_payment.html')

# タスク・支出追加機能
@login_required
def add(request):
  if request.method == 'POST':
    task = Task()
    task.title = request.POST.get('title')
    task.date = request.POST.get('date')
    task.start_time = request.POST.get('start_time')
    task.end_time = request.POST.get('end_time')
    task.method = request.POST.get('method')
    task.price = request.POST.get('price')
    task.user_id = CustomUser.objects.get(id=request.user.id)
    task.save()
  return redirect('user')

# 支出一覧
@login_required
def payment(request):
  payments = Task.objects.filter(user_id=request.user.id).order_by('-date')
  total_price = 0
  for payment in payments:
    total_price += payment.price
  params = {
    'payments': payments,
    'total_price': total_price
  }
  return render(request, 'task_app/payment.html', params)

# 支出削除機能
@login_required
def delete_payment(request, num):
  if num:
    task = Task.objects.get(pk=num)
    task.delete()
  return redirect('payment')

# 支出更新機能
class PaymentUpdateView(UpdateView):
  model = Task
  fields = ['title', 'date', 'method', 'price']
  template_name_suffix = '_update_paymentform'
  success_url = reverse_lazy('payment')

# カレンダー
class WeekCalendar(WeekWithScheduleMixin, TemplateView):
  template_name = 'task_app/index.html'
  model = Task
  date_field = 'date'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    calendar_context = self.get_week_calendar()
    context.update(calendar_context)
    return context

# タスク一覧
@login_required
def task(request):
  tasks = Task.objects.filter(user_id=request.user.id).order_by('-date', 'start_time')
  params = {
    'tasks': tasks,
  }
  return render(request, 'task_app/task.html', params)

# タスク更新機能
class TaskUpdateView(UpdateView):
  model = Task
  fields = ['title', 'date', 'start_time', 'end_time', 'method', 'price']
  template_name_suffix = '_update_taskform'
  success_url = reverse_lazy('user')
  
# タスク削除機能
@login_required
def delete_task(request, num):
  if num:
    task = Task.objects.get(pk=num)
    task.delete()
  return redirect('user')