#!/bin/bash
# Render build script

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🔄 Running migrations..."
python manage.py migrate --noinput

echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo "📚 Loading seed content (if database is empty)..."
TOPIC_COUNT=$(python manage.py shell -c "from forum.models import Topic; print(Topic.objects.count())" 2>/dev/null | tail -1)

if [ "$TOPIC_COUNT" = "0" ]; then
    echo "✓ Database is empty, loading seed content..."
    python manage.py load_seed_content
else
    echo "✓ Database already has $TOPIC_COUNT topics, skipping seed"
fi

echo "✅ Build complete!"
