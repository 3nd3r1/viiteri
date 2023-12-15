#!/bin/sh

# sovelluksen käynnistys tuotannossa

poetry run python viiteri/utils/initialize_db.py
poetry run gunicorn -w 4 'viiteri.app:create_app()' --bind 0.0.0.0:80