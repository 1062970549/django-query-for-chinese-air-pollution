import os
import time
while True:
    os.chdir('/root/Projects/django-query-for-chinese-air-pollution')
    os.system('python manage.py shell < automatic.py')
    time.sleep(3600)
