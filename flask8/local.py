"""
    数据池连接
"""
from DBUtils.PooledDB import PooledDB
import pymysql
import threading


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
        self.local = threading.local()

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

    # 进阶-加上进程
    def __enter__(self):
        conn, cursor = self.open()
        rv = getattr(self.local, 'stack', None)
        if not rv:
            self.local.stack = [(conn, cursor), ]
        else:
            rv.append((conn, cursor))
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        rv = getattr(self.local, 'stack', None)
        if not rv:
            return
        conn, cursor = self.local.stack.pop()
        conn.close()
        cursor.close()


db = PoolDB()

# ############# 使用
with db as c1:
    c1.execute('select 1')