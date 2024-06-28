#!/bin/bash

set -e  # Exit immediately on error

# Wait for Postgres to be ready (optional)
while ! /usr/bin/pg_isready -h postgres -U postgres -d task_manager; do
  echo "Waiting for postgres..."
  sleep 2
done

# Apply database migrations
python manage.py makemigrations && python manage.py migrate

# Load initial data (optional)
if [ -f "data/initial.json" ]; then
  python manage.py loaddata data/initial.json
fi

# Start the Django development server (or custom command)
exec "$@"
