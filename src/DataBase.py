# coding=utf-8
import pymysql
import time
import datetime
import uuid
'''
数据库类
数据库的连接，数据的增删改查
'''

class DataBase():
    def __init__(self):
        self.host=""
        self.user="root"
        self.password=""
        self.db="word"
        self.port=3306

    def connect(self):
        '''
        连接数据库
        :return: conn，cursor
        '''
        conn = pymysql.connect(self.host,self.user,self.password,self.db,self.port)
        cursor = conn.cursor()
        return conn,cursor

    def insert_word(self,uuid,word,kind):
        '''
        插入数据
        :param uuid:语料基于时间戳的id
        :param word: 语料
        :param kind: 种类
        :param time: 时间
        :return: 布尔型数据
        '''
        if(self.test_connect()):
            conn,cursor = self.connect()
            sql="INSERT INTO `word` (`uuid`, `word`, `kind`, `time`, `status`) VALUES (%s,%s,%s,%s,%s)"
            try:
                time=datetime.datetime.now()
                cursor.execute(sql,(uuid,word,kind,str(time),'1'))
                conn.commit()
                return True
            except:
                conn.rollback()
                return False
            cursor.close()
            conn.close()

        else:
            print('数据库连接失败')
            return False


    def test_connect(self):
        '''
        测试数据库连接
        :return: 成功返回True 失败返回False
        '''
        try:
            conn,cursor = self.connect()
            conn.close()
            cursor.close()
            return True
        except:
            return False


    def get_word(self):
        '''
        获取语料用
        :return: 返回语料文本与uuid
        '''
        if(self.test_connect()):
            conn,cursor = self.connect()
            sql = "select `uuid`,`word` from `word` where `status` = '1' limit 1"
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                for row in result:
                    uuid = row[0]
                    text = row[1]

                if(self.set_status(uuid)):
                    return str(uuid),str(text)
                else:
                    print('无法更新语料状态')
            except:
                conn.rollback()
                print('sql语句执行失败')
            conn.close()
        else:
            print('数据库连接失败')


    def set_status(self,uuid):
        '''
        讲读取的语料状态设置为已读取
        :param uuid: 语料id
        :return: bool
        '''
        if(self.test_connect()):
            conn,cursor = self.connect()
            sql = "update `word` set `status` = 1 where uuid = %s"
            try:
                cursor.execute(sql,(str(uuid)))
                conn.commit()
                return True
            except:
                conn.rollback()
                return False
            conn.close()
        else:
            print('数据库连接失败')
            return False

if __name__ == '__main__':

    #print(DataBase().insert_word('1','3月9日某某对某某作出指示','新闻'))
    print(DataBase().test_connect())
