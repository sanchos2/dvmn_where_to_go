# Description

This is a learning project from [devman](https://dvmn.org/modules/django/) (lesson 1)

[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Build Status](https://travis-ci.org/sanchos2/dvmn_where_to_go.svg?branch=main)](https://travis-ci.org/sanchos2/dvmn_where_to_go)

[Project demo version](https://sanchos2004.pythonanywhere.com/)

[Admin panel](https://sanchos2004.pythonanywhere.com/admin/)

## How to deploy

Install python3

```sh
sudo apt install python3
sudo apt install python3-pip
```

Download the project, create virtual environment and activate it, install dependencies

```sh
git clone https://github.com/sanchos2/dvmn_where_to_go.git
cd dvmn_where_to_go
python3 -m venv venv
source venv/bin/activate.sh
pip3 install -r requirements.txt
```

Make migrations

```sh
python manage.py migrate
```

Create site admin

```sh
python manage.py createsuperuser
```

Collect static files to a static root

```sh
python manage.py collectstatic
```

Add environment variables:

```
DB_ENGINE=django.db.backends.postgresql    or other db backend see Django Docs 
DB_HOST=database server address
DB_PORT=database server port
DB_NAME=database name
DB_USER=database user
DB_PASSWORD=database password
SECRET_KEY=secret key
DEBUG=0(False) or 1(True)
```
note: on production environment setup DEBUG to 0(False)


## How to run

Run project

```sh
python manage.py runserver 127.0.0.1:8000
```

Use http://127.0.0.1:8000 to browse a project


## How to load data from json

Open console and run command

```sh
python manage.py load_place http://file_url.json
```

JSON file structure

```json
{
    "title": "Place name",
    "imgs": [
        "URL to image file"
    ],
    "description_short": "Short description",
    "description_long": "Detailed description",
    "coordinates": {
        "lng": "37.61171499999998",
        "lat": "55.81972699999998"
    }
}
```
