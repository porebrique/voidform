#!/bin/bash

python manage.py  dumpdata auth.User blog  --indent 4 > fixtures/initial_data.json

