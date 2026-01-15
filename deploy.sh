#!/bin/bash
# Render deployment script

echo "🚀 Deploying to Render..."

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Load seed content (only if database is empty)
TOPIC_COUNT=$(python manage.py shell -c "from forum.models import Topic; print(Topic.objects.count())" 2>/dev/null | tail -1)

if [ "$TOPIC_COUNT" -eq "0" ]; then
    echo "📚 Database is empty, loading seed content..."
    python manage.py load_seed_content
else
    echo "✓ Database already has $TOPIC_COUNT topics, skipping seed"
fi

echo "✅ Deployment complete!"
