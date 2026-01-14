#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Önce Django ve diğer her şeyi yükle
pip install -r requirements.txt

# 2. Statik dosyaları topla
python manage.py collectstatic --noinput

# 3. Veritabanını güncelle (Burada yapıyoruz ki hata vermesin)
python manage.py migrate --noinput