#!/bin/bash
set -e
LOGFILE=/home/vagrant/api_fake/deploy/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=2 # idealmente deve ser 2n + 1 (n = qtd de processadores)
USER=www-data
GROUP=www-data
cd /home/vagrant/api_fake
test -d $LOGDIR || mkdir -p $LOGDIR
. /etc/default/locale
export LANG
export LC_ALL
exec /var/.virtualenvs/api_fake/bin/gunicorn api_faker.wsgi -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE \
  --timeout=1800

