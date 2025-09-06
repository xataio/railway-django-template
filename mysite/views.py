from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.conf import settings


def home(request):
    """
    Home view that displays PostgreSQL version to confirm database connection.
    """
    try:
        # Execute a simple query to get PostgreSQL version
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            postgres_version = cursor.fetchone()[0]
        
        # Get database connection info (without sensitive data)
        db_info = {
            'engine': settings.DATABASES['default']['ENGINE'],
            'name': settings.DATABASES['default']['NAME'],
            'host': settings.DATABASES['default']['HOST'],
            'port': settings.DATABASES['default']['PORT'],
        }
        
        context = {
            'postgres_version': postgres_version,
            'db_info': db_info,
            'connection_successful': True,
        }
        
        return render(request, 'home.html', context)
        
    except Exception as e:
        context = {
            'error': str(e),
            'connection_successful': False,
        }
        return render(request, 'home.html', context)
