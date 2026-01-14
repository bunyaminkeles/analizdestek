#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. ADIM: ÖNCE PAKETLERİ YÜKLE (Burası en başta olmalı!)
pip install -r requirements.txt

# 2. ADIM: SONRA DJANGO KOMUTLARINI ÇALIŞTIR
python manage.py collectstatic --noinput