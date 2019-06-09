# Use PyInstaller to run executable web app

## Clone the repository

```bash
$ git clone https://github.com/ferreolgodebarge/flask-restplus-boilerplate.git
```

## Install requirements

1. Enter the repository:

```bash
$ cd flask-resplus-boilerplate
```

2. Create a virtualenv:

```bash
# Create a virtual environment
$ virtualenv venv

# Linux
$ . venv/bin/activate

# Windows
$ venv\Scripts\activate.bat
```

2. Install build requirements:

```bash
# Linux
$ pip install -r integration/requirements.txt

# Windows
$ pip install -r integration\requirements.txt
```

## Test locally the application


1. With `flask` command line:

```bash
# Linux
$ export FLASK_APP=application.app:app
$ flask run

# Windows
$ set FLASK_APP=application.app:app
$ flask run
```

2. With `python`:

```bash
# Linux
$ export PYTHONPATH=.
$ python application/app.py

# Windows
$ set PYTHONPATH=.
$ python application\app.py
```

## Run PyInstaller command

```
$ pyinstaller -y --clean app.spec
```

The folder `./dist/app/` will contain the binary and all the depencies.

You can run : `app` or `app.exe` in order to run the application.

## Configure app

1. Create a file `settings.cfg`

```conf
SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
VERSIONS="v1"
```

2. Put it in `./dist` location

3. Restart the application

Configuration List:

```conf
SQLALCHEMY_DATABASE_URI=''
VERSIONS=''
```
