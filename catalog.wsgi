#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, 'var/www/coffeeshops')

from catalog import app as application
from catalog.database_setup import create_database
from catalog.database_populator import populate_database

application.config['DATABASE_URL'] = 'sqlite:////var/www/coffeeshops/catalog/coffeeshopmenu.db'
application.config['OAUTH_SECRETS_LOCATION'] = '/coffeeshops/catalog/'

# Create database and populate it, if not already done so.
create_database(application.config['sqlite:////var/www/coffeeshops/catalog/coffeeshopmenu.db')
populate_database()
