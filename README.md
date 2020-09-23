# project108_cheering
プロジェクト108で作成している最初のアプリケーションです

開発用の環境として作成していきます。
今後の課題として、デプロイ用の環境も意識します。

開発環境をすぐに整えられるよう、
dockerを使用します。

---
## 使用方法
### gitでクローンを行う。
~~~
$ git clone https://github.com/rnakamura-sky/project108_cheering.git
~~~
### データベース用にmigrateする
docker内でも出来ますが、ここでは端末上で行ってしまいます。
実行する前にpythonを使用する環境に下記のライブラリが存在することを確認してください。
- django
- celery
- django-celery-results
- redis
- requests

~~~
# manage.py が存在するフォルダに移動します。
$ cd api/project108
$ python manage.py migrate


# ユーザーを作成しないと動作しないので、スーパーユーザーを作成します。
# 下記のコマンド後聞かれる情報を入力して作成してください。
$ python manage.py createsuperuser
~~~

### docker-compose でビルドする
dockerが端末にインストールされている必要があります。
~~~
# docker-compose.ymlが存在するフォルダに移動します。
$ cd ../../
$ docker-compose build --no-cache

# proxyの設定が必要な場合は引数で指定してください。
$ docker-compose build --no-cache --build-arg http_proxy=http://プロキシサーバー:ポート --build-arg https_proxy=https://プロキシさーばー:ポート
~~~

### サーバー起動
~~~
# docker-compose.ymlが存在するフォルダで実行してください。
$ docker-compose up -d
~~~

必要となる情報の登録は、`/admin/`で設定することができます。

`/account/login/`にアクセスし、ログインすることで一連の動作を
行うことが出来ます。



構成
- アプリケーションコンテナ
- redis用コンテナ
- 非同期処理用コンテナ(celery)
- テスト用マシーン

デプロイの環境は下記を想定しています。
- Webコンテナ(apatch)
- APIコンテナ(uwsgi+python(django))
- DBコンテナ(mysql)
- ブローカーコンテナ(redis)
- 非同期処理用コンテナ(celery)

