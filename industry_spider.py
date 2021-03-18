import pymysql
import json
url = 'https://backend.fyzct.com/dict/api/1/1/dict-values/XXT_CODE_001'
ua = {'spaceUri':'参数请自行抓包'}
import requests
html = requests.get(url,headers=ua)
data = []
for cc in json.loads(html.content.decode('utf-8'))['data']:
    data.append((cc['description'],cc['value']))
insert_sql = 'INSERT INTO industry_code (code_name,code_id) VALUES (%s,%s);'
db = pymysql.connect('localhost','root','morning321','zhizaoshe_app')
cursor = db.cursor()
cursor.executemany(insert_sql,data)
db.commit()