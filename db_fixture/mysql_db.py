# coding=utf-8

from pymysql import connect,cursors
from pymysql.err import OperationalError
import os,time
import configparser as cparser

# ===========读取 db_config.ini文件设置============

baser_dir = str(os.path.dirname(os.path.dirname(__file__)))
baser_dir = baser_dir.replace('\\','/')
file_path = baser_dir + "/db_config.ini"
print (file_path)

cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get("mysqlconf",'host')
port = cf.get("mysqlconf","port")
db = cf.get("mysqlconf","db_name")
user = cf.get("mysqlconf",'user')
password = cf.get("mysqlconf","password")

# =========封装mysql基本操作==============
class DB:

    def __init__(self):
        try:
            # 链接数据库
            self.conn = connect(host=host,
                                port=int(port),
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4')
        except OperationalError as e:
            print ("mysql error %d: %s" %(e.args[0],e.args[1]))

    # 清除表数据
    def clear(self,table_name):
        real_sql = "delete from " + table_name + ";"
        with self.conn.cursor() as cursor:
            cursor.execute("set foreign_key_checks=0")   # 取消外键约束
            cursor.execute(real_sql)
        self.conn.commit()

    # 插入表数据
    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key] = "'" +str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print (real_sql)

        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()

    # 关闭数据库链接
    def close(self):
        self.conn.close()

if __name__ == '__main__':
    past_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    db = DB()
    table_name = "sign_guest"

    data = [{'id': 1, 'name': '红米', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
            'start_time': '2016-08-20 00:25:42','create_time':'2016-08-20 00:25:42'},
            {'id': 1, 'realname': 'alen', 'phone': 13511001100, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 1,
             'create_time': past_time}]

    db.clear(table_name)
    db.insert(table_name,data[1])
    db.close()














