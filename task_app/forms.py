from django import forms
from .models import Task
from django.core.exceptions import ValidationError

class MoneyTaskForm(forms.ModelForm):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.label_suffix = " "
    for field in self.fields.values():
      field.widget.attrs['placeholder'] = field.label
      # field.label = ''
      
  class Meta:
    model = Task
    fields = ['title', 'date', 'start_time', 'end_time', 'method', 'price']
    labels = {
      'title': 'タイトル',
      'date': '日付',
      'start_time': '開始時刻',
      'end_time': '終了時刻',
      'method': '支払い方法',
      'price': '金額'
    }
    widgets = {
      'date': forms.NumberInput(attrs={
        "type": "date"
      }),
      'start_time': forms.NumberInput(attrs={
        "type": "time"
      }),
      'end_time': forms.NumberInput(attrs={
        "type": "time"
      }),
    }
    
  def clean_end_time(self):
    start_time = self.cleaned_data['start_time']
    end_time = self.cleaned_data['end_time']
    if end_time <= start_time:
      raise ValidationError('終了時間は、開始時間よりも後にしてください')
    return end_time