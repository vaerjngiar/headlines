activate_this = '/var/www/headlines/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/headlines')

from myfirstapp import app as application

