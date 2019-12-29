activate_this = 'C:/Users/PeterChen/Envs/Self_Introduction_Website/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Users/PeterChen/Envs/Self_Introduction_Website/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('D:/PycharmProjects/Self_Introduction_Website')
sys.path.append('D:/PycharmProjects/Self_Introduction_Website/Self_Introduction_Website')

os.environ['DJANGO_SETTINGS_MODULE'] = 'Self_Introduction_Website.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Self_Introduction_Website.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()