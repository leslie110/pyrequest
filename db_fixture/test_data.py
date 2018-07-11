# coding=utf-8

from db_fixture.mysql_db import DB
import time

past_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

#创建测试数据
datas = {
    # 发布会数据
    'sign_event':[
        {'id': 1, 'name': '红米1', '`limit`': 2000, 'status': 1,
         'address': '北京会展中心','start_time': '2016-08-20 00:25:42','create_time':past_time},
        {'id': 2, 'name': '红米2', '`limit`': 2000, 'status': 1,
         'address': '北京会展中心','start_time': '2016-08-20 00:25:42','create_time':past_time},
        {'id': 3, 'name': '红米3', '`limit`': 2000, 'status': 1,
         'address': '北京会展中心','start_time': '2016-08-20 00:25:42','create_time':past_time},
        {'id': 4, 'name': '红米4', '`limit`': 2000, 'status': 1,
         'address': '北京会展中心','start_time': '2016-08-20 00:25:42','create_time':past_time},
        {'id': 5, 'name': '红米5', '`limit`': 2000, 'status': 1,
         'address': '北京会展中心','start_time': '2016-08-20 00:25:42','create_time':past_time}
    ],
    # 嘉宾表数据
    'sign_guest':[
        {'id':1,'realname':'alen','phone':13511001100,'email':'alen@mail.com','sign':0,'event_id':1,'create_time':past_time},
        {'id':2,'realname':'has sign','phone':13511001101,'email':'sign@mail.com','sign':1,'event_id':1,'create_time':past_time},
        {'id':3,'realname':'tom','phone':13511001102,'email':'tom@mail.com','sign':0,'event_id':5,'create_time':past_time},
        {'id':4,'realname':'jay','phone':13500000000,'email':'jay@mail.com','sign':0,'event_id':2,'create_time':past_time}
    ],
}

# 将测试数据插入表
def init_data():
    db = DB()
    for table,data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table,d)
    db.close()
if __name__ == '__main__':
    init_data()



