import os.path

from catalog import app
from catalog.database_setup import create_db
from catalog.populate_database import populate_database

if __name__ == '__main__':
    # App configuration
    app.config['DATABASE_URL'] = 'sqlite:///coffeeshopmenu.db'
    app.config['UPLOAD_FOLDER'] = '/vagrant/catalog/item_images'
    app.config['OAUTH_SECRETS'] = ''

    app.secret_key = 'super_secret_key'  # This needs changing in production env

    if app.config['DATABASE_URL'] == 'sqlite:///itemcatalog.db':
        if os.path.isfile('itemcatalog.db') is False:
            create_db(app.config['DATABASE_URL'])
            populate_database()
    else:  
        create_database(app.config['DATABASE_URL'])
        populate_database()

    app.debug = True
    app.run(host='0.0.0.0', port=10080)
