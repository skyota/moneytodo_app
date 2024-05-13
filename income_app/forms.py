from django import forms
from .models import Income

class IncomeForm(forms.ModelForm):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.label_suffix = " "
    for field in self.fields.values():
      field.widget.attrs['placeholder'] = field.label
      # field.label = ''
      
  class Meta:
    model = Income
    fields = ['title', 'date', 'price']
    labels = {
      'title': 'タイトル',
      'date': '日付',
      'price': '金額'
    }
    widgets = {
      'date': forms.NumberInput(attrs={
        "type": "date"
      })
    }