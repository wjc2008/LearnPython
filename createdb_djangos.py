import pymysql  # 在这儿用python 建立了第一个数据库world111

# 打开数据库连接
# 注意password的密码是你刚刚设置的，port=3306是MySql默认的端口号
db = pymysql.connect(host='localhost', user='root',
                     password='123456', port=3306)
print(db)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
print(cursor)
# SQL 插入语句
cursor.execute("CREATE DATABASE djangos DEFAULT CHARACTER SET UTF8MB4")
