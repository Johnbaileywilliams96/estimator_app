#!/bin/bash

rm db.sqlite3
rm -rf ./backendapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations backendapi
python3 manage.py migrate backendapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

