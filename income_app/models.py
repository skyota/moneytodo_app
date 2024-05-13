from django.db import models
from django.contrib.auth import get_user_model

class Income(models.Model):
  # タイトル
  title = models.CharField("タイトル", max_length=100)
  # 日付
  date = models.DateField("日付")
  # 金額
  price = models.IntegerField("金額")
  # ユーザーとの紐付け
  user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)