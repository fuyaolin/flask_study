"""
    数据池连接
"""
from DBUtils.PooledDB import PooledDB
import pymysql


class PoolDB(object):
    def __init__(self):
        self.POOL = PooledDB(
            creator=pymysql,
            host='localhost',
            port='3306',
            database='xxx',
            user='root',
            password='xxx',
            charset='utf8',
            # 初始化连接池时创建的连接数, 0表示不创建
            mincached=0,
            # 池中空闲连接的最大数量
            maxcached=6,
            # 被允许的最大连接数, 0表示不限制
            maxconnections=0,
            # 连接数达到最大时，新连接是否可阻塞
            blocking=True,
        )

    def open(self):
        conn = self.POOL.connection()
        cursor = conn.cursor()
        return conn, cursor

    def fetchall(self, sql, *args):
        conn, cursor = self.open()
        cursor.execute(sql, *args)
        result = cursor.fetchall()
        self.close(conn, cursor)
        return result

    def fetchone(self, sql, *args):
        conn, cursor = self.open()
        cursor.execute(sql, *args)
        result = cursor.fetchone()
        self.close(conn, cursor)
        return result

    def other(self, sql, *args):
        conn, cursor = self.open()
        result = cursor.execute(sql, *args)
        cursor.commit()
        self.close(conn, cursor)
        return result

    def close(self, conn, cursor):
        conn.close()
        cursor.close()


db = PoolDB()
