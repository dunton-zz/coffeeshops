#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/coffeeshops')

from catalog import app as application
from catalog.database_setup import create_database
from catalog.database_populator import database_populator

application.secret_key = 'super_secret_key'  

application.config['DATABASE_URL'] = 'sqlite:///coffeeshopmenu.db'
application.config['OAUTH_SECRETS_LOCATION'] = '/coffeeshops/catalog/'

# Create database and populate it, if not already done so.
create_database(application.config['sqlite:///coffeeshopmenu.db'])
populate_database()
