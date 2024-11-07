import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogPost.settings')

# Create the WSGI application object
application = get_wsgi_application()

# Get the port from the environment variable (Render automatically provides it)
port = os.environ.get('PORT', '8000')  # Defaults to 8000 if not set

# Print the port for debugging (optional, but useful)
print(f"Running on port: {port}")
