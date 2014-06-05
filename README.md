#中国各城市空气质量查询 
A Django query for Chiese Air Pollution Conditions

##介绍
1. 利用 Django， 调用 [PM25.in](http://www.pm25.in/) 的相关数据借口，实现一个简单的自用中国 PM2.5 空气质量查询功能。
2. 本 respository 中未提供 [PM25.in](http://www.pm25.in/) 的 API 接口，请自行发邮件申请。
3. [PM25.in](http://www.pm25.in/) 提供的 API 文档： [API Documentations](http://www.pm25.in/api_doc)

##基本功能

1. 通过 API 获取中国各大城市空气质量数据：<a href="http://127.0.0.1:8000/getdata/">http://127.0.0.1:8000/getdata/</a>
2. 获取数据库中所有数据：[http://127.0.0.1:8000/index/](http://127.0.0.1:8000/index/)
