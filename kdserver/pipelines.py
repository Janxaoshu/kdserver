import MySQLdb
import pymysql
from scrapy.utils.project import get_project_settings


def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='root',
        charset='utf8',
        db='kdsql',
        use_unicode=False
    )
    print(1131313)
    return conn


class KdServerPipeline(object):
    def process_item(self,item):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        # sql = 'insert into message(name, url)  values (%s,%s)'
        print('=======================================================')
        sql = "insert into message(name,url) values(%s,%s)"
        params = ("title", "http://www.baidu.com")
        try:
            cursor.execute(sql, params)
            dbObject.commit()
        except Exception as e:
            print(e)
            dbObject.rollback()

        return item
