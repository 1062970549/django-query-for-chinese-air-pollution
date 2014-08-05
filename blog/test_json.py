import json

content = open('all_cities.json','r')
data = json.loads(content.read())

# for key in data[1].keys():
	# print key
# for city in data:

# 	print city.get('area'),'-',city.get('position_name'),'- PM 2.5:',city.get('pm2_5'),'time:',city.get('time_point')


print type(data[1].get('time_point'))

