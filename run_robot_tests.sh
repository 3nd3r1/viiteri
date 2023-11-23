#!/bin/bash

# käynnistetään Flask-palvelin taustalle
poetry run invoke debug &

# odetetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5001/ping)" != "200" ]];
  do sleep 1;
done

# suoritetaan testit
poetry run invoke robottest

status=$?

# pysäytetään Flask-palvelin portissa 5001
kill $(lsof -t -i:5001)

exit $status