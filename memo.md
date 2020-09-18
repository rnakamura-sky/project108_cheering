# やったことをテキストで羅列しておきます。

## 仮想環境作成(venv)

## venv有効化

## pip 最新化

## 必要なライブラリをインストール  
ここではrequirements.txtを使用してインストールする。
~~~
$ pip install -r requirements.txt
~~~

## gitインストール
gitが必要になるので、インストールするけど私はすでにインストールしているのでシカトする。

## githubアカウント作成
githubのアカウント作成が必要ですが、私はすでに持っているのでシカトする。

## 【無視】PythonAnywhereインストール
このリストdjangogirlsをもとに作成してるので、pythonanywhereをインストールする手順ですが、ここでは使わないので無視する。

## プロジェクト作成  
project108にしておきます。
~~~
$ django-admin startproject project108 .
~~~

## 環境に合わせて設定変更
~~~python
# project108/settings.py
TIME_ZONE = 'Asia/Tokyo'
LANGUAGE_CODE = 'ja'
~~~

## 静的ファイルのパスを追加
静的ファイルは、実際運用する時にdjangoからは提供しません。  
例えば、本番環境はapatch->uwsgi->djangoといった流れでやり取りを行いますが、apatchで静的ファイルは取得するようにするのがデフォルトスタンダードのようなので、それに対応するためにこの設定を入れます。
ちなみに、開発の場合は`python manage.py  runserver`としてdjangoのみでやり取りするので開発だけの場合は必要ありません。  
分かりやすいよう、STATIC_URL設定の下に書いておきましょう。
~~~python
# project108/settings.py
# 上の方にimport osを追記しておいてください。
STATIC_URL='/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
~~~

## DBの設定
 ここでデータベースの設定変更するべきですが(mysqlに)ちょっと後回しにしておきます。（MySQLサーバーを立てないといけないからね。。。）

## gitの設定
gitを使って管理しましょう。ということでここで設定していきます。
~~~
$ git init
$ git config --global user.name "Your Name"
$ git config --global user.email you@example.com
~~~
このリポジトリだけで使用したい設定の場合は
するよう--globalを指定しないで実行した。

## .gitignoreを作成
gitで管理する時に、自動生成されるファイルや、データベース等の
アップロードしたくないファイルを設定します。
windowsの場合は、`.`から始まるファイルはエクスプローラから作成できないので、VSCodeを使用するか、適当な名前で作成したあとコマンドでリネームして作成してください。
~~~
# .gitignore
*.pyc
*~
__pycache__
venv
db.sqlite3
/static
.DS_Store
/.vscode
~~~

## ローカルのリポジトリに変更を保存
~~~
# すべての変更を追加
$ git add --all .

# ローカルのリポジトリへ変更をコミット
$ git commit -m "Django初期設定"

# 状態確認
$ git status

~~~

# GitHubにリモートリポジトリ作成
- ブラウザでGitHubへ
- GitHubにログイン
- 右上にある「＋」をクリックして「New repository]を選択
- 「Repository name」に名前をつける
- Descriptionにリポジトリの概略をつける
- **Initialize this repository with a README.**にチェックをつける  
    これは公式のイントロダクションでつけてるので。
- 作成できたら、リポジトリのパスを取得してね。

# GitHub上のリポジトリをローカルと結びつけます。
その前に、、、
プロキシがある環境の場合はGitにプロキシの設定が必要です。
~~~
$ git config --global https.proxy http://プロキシサーバー:ポート
~~~
以下がメインのコマンド！
~~~
$ git remote add origin https://github.com/rnakamura-sky/hello-world.git
$ git push -u origin master
~~~
するとユーザとパスワードを求められるので入力しましょう。

