# Pythonのイメージから作成
FROM python:3

# python環境変数の１つ。コンソールの標準出力(stdout)と標準エラー出力(stderr)がエラー発生時にすぐに出力されるようにする
ENV PYTHONUNBUFFERED 1

# appユーザのDjangoディレクトリを作成
ENV APP_HOME = /usr/src/app

# コンテナで/codeディレクトリ作成
# RUN mkdir /code
RUN mkdir $APP_HOME

# ワークディレクトリを設定する(/codeで作業)
# WORKDIR /code
WORKDIR $APP_HOME

# codeディレクトリにrequirements.txtを追加する
# ADD requirements.txt /code/
ADD requirements.txt $APP_HOME

# requirements.txtに記載しているものをinstallする
RUN pip install -r requirements.txt

# プロジェクトを追加する
# ADD . /code/
ADD . $APP_HOME