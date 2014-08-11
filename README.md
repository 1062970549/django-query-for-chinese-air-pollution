A Django query for Chiese Air Pollution Conditions
===


Introduction
----
1. This is a Django website using ```urllib``` to scratch air pollution data from [PM25.in](http://www.pm25.in/)'s APIs，some template to show the data
2. The Chinese Air Pollution APIs from  [PM25.in](http://www.pm25.in/) could be available by sending emails to them.
3. APIs' Documentations in [PM25.in](http://www.pm25.in/): [APIs Documentations](http://www.pm25.in/api_doc)

Basic Implementation
--------------------

1. Scratching the  data of air pollution in Chinese main cities:<a href="http://127.0.0.1:8000/getdata/">http://127.0.0.1:8000/getdata/</a>
2. Get the data from the database：[http://127.0.0.1:8000/index/](http://127.0.0.1:8000/index/)

Nexp Step Features(Not done yet)
------------------------------
1. Grab and store the historical daily data from each city. 
1. Data visualization: improving the front-end design of the websites.
3. Got all the data and do the sorting and ranking of all the cities in China.
4. Improve database performance.
5. - [x] Deploy into my server.
6. - [x] Grab the latest data and delete the old ones.
7. - [x] BootStrap integration


License
-------
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)
