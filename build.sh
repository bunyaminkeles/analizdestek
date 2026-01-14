#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Paketleri yükle
pip install -r requirements.txt

# 2. Statik dosyaları topla
python manage.py collectstatic --noinput

# 3. Veritabanını güncelle
python manage.py migrate --noinput

# 4. KATEGORİLERİ KUR (İşte yeni eklediğimiz kısım)
python manage.py setup_categories