import json

r=open('aqi_ranking.json','r')
content = json.loads(r.read())
keys = content[1].keys()
for key in keys:
    print key

