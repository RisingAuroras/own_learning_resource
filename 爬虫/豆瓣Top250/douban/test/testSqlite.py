#encoding=utf-8

import  sqlite3

def createTable():
    # 1.连接数据库
    conn  = sqlite3.connect("test.db") # 打开或创建数据库文件
    print("成功打开数据库")

    # 2.创建表格
    c = conn.cursor() # 拿到游标
    sql = '''
        create table company
            (id int primary key not null,
            name text not null,
            age int not null,
            address char(50),
            salary real);
    '''
    c.execute(sql)
    conn.commit()
    conn.close()
    print("创建表成功")


def insertToTable():
    conn = sqlite3.connect("test.db")
    print("成功打开数据库")
    c = conn.cursor()
    sql = '''
        insert into company(id,name,age,address,salary)
         values(1,'张三',32,'成都',8000);
    '''
    c.execute(sql)
    conn.commit()
    conn.close()
    print("插入成功")
def queryData():
    conn = sqlite3.connect("test.db")
    print("数据库打开成功")
    c = conn.cursor()
    sql = "select id ,name,address from company"
    cursor = c.execute(sql)
    for row in cursor:
        print(row)

    print("查询成功")

    conn.close()


if __name__ == '__main__':
    # createTable()
    # insertToTable()
    queryData()