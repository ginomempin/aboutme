#!/usr/bin/env bash

if [ ! -e "static/css/home.css" ]
then
    python -mscss < assets/scss/home.scss > static/css/home.css
fi

export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
