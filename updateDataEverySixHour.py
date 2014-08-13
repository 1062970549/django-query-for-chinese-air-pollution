import os
import time
while True: 
    os.chdir('/root/Projects/django-query-for-chinese-air-pollution')
    os.system('python manage.py shell < automatic_every6hour.py')
    time.sleep(21600)
