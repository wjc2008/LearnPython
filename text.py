import pymysql

# 打开数据库连接
# 注意password的密码是你刚刚设置的，port=3306是MySql默认的端口号
db = pymysql.connect(host='localhost', user='root',
                     password='123456', port=3306)
print(db)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
print(cursor)
# SQL 插入语句
cursor.execute("CREATE DATABASE world DEFAULT CHARACTER SET UTF8MB4")
# 创建一个Myfirsttest 的数据库
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
