import os.path

from catalog import app
from catalog.database_setup import create_database
from catalog.populate_database import database_populator

if __name__ == '__main__':
    app.config['DATABASE_URL'] = 'sqlite:////var/www/coffeeshops/catalog/coffeeshopmenu.db'
    app.config['UPLOAD_FOLDER'] = '/vagrant/catalog/item_images'
    app.config['OAUTH_SECRETS'] = ''
    
    if app.config['DATABASE_URL'] == 'sqlite:////var/www/coffeeshops/catalog/coffeeshopmenu.db'
        if os.path.isfile('sqlite:////var/www/coffeeshops/catalog/coffeeshopmenu.db'):
            create_database('sqlite:////var/www/coffeeshops/catalog/coffeeshopmenu.db')
            populate_database()
    else:
        create_database()
        populate_database()

    app.debug = True
    app.run(host='0.0.0.0', port=10080)
