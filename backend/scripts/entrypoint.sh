#!/usr/bin/env bash

set -o errexit
set -o pipefail
cmd="$@"

function postgres_ready(){
python << END
import sys
import psycopg2
from decouple import config

try:
    dbname = config('RDS_DB_NAME')
    user = config('RDS_USERNAME')
    password = config('RDS_PASSWORD')
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host='postgres', port=5432)
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."
exec $cmd
