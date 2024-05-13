from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
  
  # 支払い方法の選択肢
  METHOD = (
    ('none', ''),
    ('cash', '現金'),
    ('credit', 'クレジットカード'),
  )
  
  # タイトル
  title = models.CharField("タイトル", max_length=100)
  # 日付
  date = models.DateField("日付")
  # 開始時刻
  start_time = models.TimeField("開始時刻", default='00:00')
  # 終了時刻
  end_time = models.TimeField("終了時刻", default='00:00')
  # 支払い方法
  method = models.CharField("支払い方法", max_length=20, choices=METHOD, blank = True, null = True, default='none')
  # 金額
  price = models.IntegerField("金額", default=0)
  # ユーザーとの紐付け
  user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)