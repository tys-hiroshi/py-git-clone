# git clone をまとめてにするやつ

## Usage

.vscode/settings.json のパスはいい感じにする

config_base.yml を 同ディレクトリにコピーして config.ymlにする

config,yml を以下の通り設定する。

1.CloneRepositoryListにリポジトリのURLを記載する
2.CloneDestinationBaseDirPath はCloneしたいディレクトリ(Windows のパスなら```\``` は ```\\``` にすること)

3.以下のコマンドを実行する

```
pipenv install
pipenv shell
python main.py
```


## Windows 10

環境変数(ユーザ)に以下を追加する

```
C:\Users\Tashiro\AppData\Local\Programs\Python\Python38
C:\Users\Tashiro\AppData\Local\Programs\Python\Python38\Scripts
```

Pathが通っていることを確認

```
python --version
pip --version
```

Vscode をAdministrator で実行し、Terminal(PowerShell)を立ち上げる

pip install --upgrade pip


pip が最新になったので、Vscode(PS)はAdministratorでなくてもよい

## install pipenv

```
pip install pipenv
```


```pipenv``` と打って使い方が表示されればOK

```
pipenv --python 3.8
```

## install pypi package

```
pipenv install GitPython
```


```
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```


仮想環境が ```C:\Users\[user name]\.virtualenvs\[hogehoge]``` に作られてしまうので、変えたい。(以下をやったけど変わらない)

```
$ export PIPENV_VENV_IN_PROJECT=1  # Windowsは`set PIPENV_VENV_IN_PROJECT=1`
```

```
$ export WORKON_HOME=~/.venvs    # Windowsは`set WORKON_HOME=~/.venvs`

$ echo %WORKON_HOME%
```

https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a

https://pipenv-ja.readthedocs.io/ja/translate-ja/advanced.html#custom-virtual-environment-location


```
python -m venv .venv
source .venv/bin/activate
```

