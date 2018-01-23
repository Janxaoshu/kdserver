import pymysql
from scrapy.utils.project import get_project_settings


class db():
    def __init__(self):
        self.settings = get_project_settings()  # 获取settings配置，设置需要的信息

        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.passwd = self.settings['MYSQL_PASSWD']
        self.db = self.settings['MYSQL_DBNAME']

        # 连接到mysql，连接到具体的数据库

    def connectDatabase(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               db=self.db)  # 要指定编码，否则中文可能乱码
        print('connect pymysql success')
        return conn

    def insert(self, sql, params):  # 注意这里params要加*,因为传递过来的是元组，*表示参数个数不定
        conn = self.connectDatabase()

        cur = conn.cursor();
        cur.execute(sql, params)
        conn.commit()  # 注意要commit
        cur.close()
        conn.close()


class helper():
    def __init__(self):
        self.db = db()

    # 测试创建数据库（settings配置文件中的MYSQL_DBNAME,直接修改settings配置文件即可）
    def testCreateDatebase(self):
        self.db.createDatabase()
        # 测试创建表

    def testCreateTable(self):
        sql = "create table message(id int primary key auto_increment,name varchar(50),url varchar(200))"
        self.db.createTable(sql)

    def testInsert(self):
        sql = "insert into message(name,url) values(%s,%s)"
        params = ("title", "http://www.kudou.com")
        self.db.insert(sql, params)  # *表示拆分元组，调用insert（*params）会重组成元组

    def testUpdate(self):
        sql = "update testtable set name=%s,url=%s where id=%s"
        params = ("update", "update", "1")
        self.db.update(sql, *params)

    def testDelete(self):
        sql = "delete from testtable where id=%s"
        params = ("1")
        self.db.delete(sql, *params)


if __name__ == "__main__":
    testDBHelper = helper()
    testDBHelper.testInsert()
