# release.sh
#!/bin/bash

set -e
# Apply database migrations
python manage.py migrate
