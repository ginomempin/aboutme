import os

SCSS_ASSET_DIR = 'assets'
SCSS_STATIC_DIR = 'static'

# The site does not really need CSRF protection since
# there are no requests and posted data (everything's
# static). Also, the value shouldn't also be available
# on a public repo.
# This is just here for reference and for future impl.
SECRET_KEY = os.urandom(24)
