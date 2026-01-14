#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

# --- İŞTE SİHİRLİ SATIR BU ---
python create_superuser.py