from django.contrib import admin
from django.contrib.auth import get_user_model

# get_user_model()は、settings.pyでAUTH_USER_MODELに設定されているモデルを取得
# CustomUser = get_user_model()
# カスタムユーザが管理画面を利用できるようにする
# admin.site.register(CustomUser)
