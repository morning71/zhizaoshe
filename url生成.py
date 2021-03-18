import pymysql
import json
db = pymysql.connect('localhost','root','morning321','zhizaoshe_app')
cursor = db.cursor()

base_url = {"instName":"","industry":"{industry_code}","industryLabel":"{industry_name}","province":"{province_code}","city":"","region":"","address":"{address_name}","productPrice":"XXT_CODE_003_01,XXT_CODE_003_02,XXT_CODE_003_03,XXT_CODE_003_05,XXT_CODE_003_04,XXT_CODE_003_06","productPriceLabel":"10万以下/10-30万/30-50万/100-300万/50-100万/300万以上","application":"XXT_CODE_002_01,XXT_CODE_002_02,XXT_CODE_002_03,XXT_CODE_002_06,XXT_CODE_002_05,XXT_CODE_002_04,XXT_CODE_002_07,XXT_CODE_002_08,XXT_CODE_002_09,XXT_CODE_002_12,XXT_CODE_002_11,XXT_CODE_002_10,XXT_CODE_002_13,XXT_CODE_002_14,XXT_CODE_002_15,XXT_CODE_002_17,XXT_CODE_002_16,XXT_CODE_002_18","applicationLabel":"产品设计/工艺设计/工艺优化/生产作业/计划与调度/采购/质量控制/仓储与配送/安全与环保/销售管理/物流管理/能源管理/产品服务/人员管理/设备管理/信息安全/网络互联/文档（知识库）管理","productName":"","businessScope":"","openId":""}
select_sql1 = 'SELECT provinces,p_id,city,c_id FROM city;'
cursor.execute(select_sql1)
city_list = cursor.fetchall()
select_sql2 = 'SELECT code_name,code_id FROM industry_code;'
cursor.execute(select_sql2)
industry_list = cursor.fetchall()
data = []
for i in city_list:
    province_code = i[1]
    address_name = i[0]+ i[2]
    city = i[3]
    for j in industry_list:
        industry_code = j[1]
        industry_name = j[0]
        base_url['industry']= industry_code
        base_url['industryLabel'] = industry_name
        base_url['province'] = province_code
        base_url['address'] = address_name
        base_url['city'] = city
        url = base_url
        data.append((json.dumps(url),province_code,city,industry_code))
insert_sql = 'INSERT INTO url_list (url,p_id,c_id,u_id) VALUES (%s,%s,%s,%s);'
cursor.executemany(insert_sql,data)
db.commit()