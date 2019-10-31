import pymysql
from  etc.MysqlSetting import *



class SqlModel(object):
    def __init__(self):
        self.host = "192.168.1.152"
        self.user = "root"
        self.passwd = "123456"
        self.dbname = "FinceRobotManager"
        try:
            self.db = pymysql.connect(self.host,self.user,self.passwd,self.dbname)
        except Exception as e:
            print("数据库连接错误，错误内容%s" % e)   # 后期需替换成log形式

        self.cursor = self.db.cursor()

    def select_all(self,sql_info):
        """返回的是一个[[],[]] 如果空返回[]"""
        try:
            res = self.cursor.execute(sql_info)
            result = self.cursor.fetchall()
            if res:
                res_list = []
                for i in result:
                    res_list2 = []
                    for j in i:
                        res_list2.append(j)
                    res_list.append(res_list2)
                return res_list
            else:
                return []
        except Exception as e:
            print("数据库查询错误，错误内容:%s" % e)
        finally:
            self.cursor.close()
            self.db.close()

    def select_one(self, sql_info):
        """返回的是一个[1,1] 为空返回[]"""
        try:
            res = self.cursor.execute(sql_info)
            result = self.cursor.fetchone()
            if res:
                res_list = []
                for i in result:
                    res_list.append(i)
                return res_list
            else:
                return []
        except Exception as e:
            print("数据库查询错误，错误内容:%s" % e)
        finally:
            self.cursor.close()
            self.db.close()

    def insert_or_update(self,sql_info):
        """成功返回True,失败False"""
        try:
            self.cursor.execute(sql_info)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False
        finally:
            self.cursor.close()
            self.db.close()

    def insert(self,table,field,value):
        """成功返回True,失败False"""

        a = ()

        sql = "insert into %s%s value %s" % (table,field,value)




class Mysql_base(object):
    ''' 数据库操作基本类, 包含于业务无关的的操作方法'''
    def __init__(self, host, user, passwd, dbname, port):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.port = port
        self.conn = self.connect()


    def connect(self):
        conn = pymysql.connect(self.host, self.user, self.passwd, self.dbname, self.port)
        return conn

    def select(self, table, fields, condition, order_by=None, limit=None, desc=False):

        sql = 'SELECT {fields} from {table} WHERE {condition}'.format(
            fields=fields, table=table, condition=condition)
        print(sql)
        if order_by:
            sql = sql + ' ORDER BY {order_by}'.format(order_by=order_by)

        if desc:
            sql = sql + ' DESC'

        if limit:
            sql = sql + ' LIMIT {limit}'.format(limit=limit)

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            print('Select %d lines' % cursor.rowcount)
            cursor.close()
            self.conn.commit()
            return results
        except Exception as e:
            print("<<<<<<<<<<<<<<<<:",e)
            print('DataBase Select Error: %s' % e)
            # TODO(blkart): raise SelectError




    def select_one(self, sql_info):
        """返回的是一个[1,1] 为空返回[]"""
        try:
            cursor = self.conn.cursor()
            res = cursor.execute(sql_info)
            result = cursor.fetchone()
            if res:
                res_list = []
                for i in result:
                    res_list.append(i)
                return res_list
            else:
                return []
        except Exception as e:
            print("数据库查询错误，错误内容:%s" % e)
        finally:
            self.conn.commit()
            cursor.close()



    def select_all(self, sql_info):
        """返回的是一个[1,1] 为空返回[]"""
        try:
            print(sql_info)
            cursor = self.conn.cursor()
            res = cursor.execute(sql_info)
            result = cursor.fetchall()
            if res:
                print("====================")
                print(res)
                res_list = []
                for i in result:
                    res_list2 = []
                    for j in i:
                        res_list2.append(j)
                    res_list.append(res_list2)
                return res_list
            else:
                return []
        except Exception as e:
            print("数据库查询错误，错误内容:%s" % e)
        finally:
            cursor.close()





    def insert(self, table, values, fields=None):

        if fields:
            sql = 'INSERT INTO {table} {fields} VALUES {values}'.format(
                table=table, fields=fields, values=(tuple(values)))
            print('sql lanuager:', sql)
        else:
            sql = 'INSERT INTO {table} VALUES {values}'.format(
                table=table, values=values)

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            cursor.close()
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print('DataBase Insert Error: %s' % e)
            # TODO(blkart): raise InsertError

    def delete(self, table, condition):
        sql = 'DELETE FROM {table} WHERE {condition}'.format(
            table=table, condition=condition)

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            cursor.close()
            self.conn.commit()
        except Exception as e:
            print('DataBase Delete Error: %s' % e)
            # TODO(blkart): raise DeleteError

    def update(self, table, assignments, condition):
        sql = 'UPDATE {table} SET {assignments} WHERE {condition}'.format(
            table=table, assignments=assignments, condition=condition
        )

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            cursor.close()
            self.conn.commit()
        except Exception as e:
            print('DataBase Update Error: %s' % e)
            # TODO(blkart): raise UpdateError






#  TODO  查询 远程FRM数据库的信息  回写咱们的数据库
class Mysql_client(Mysql_base):
    ''' TODO 与业务有关的数据库操作方法'''
    def __init__(self):
        self.host = I_MYSQL_HOST
        self.user = I_MYSQL_USERNAME
        self.passwd = I_MYSQL_PASSWORD
        self.dbname = I_MYSQL_DATABASE_NAME
        self.port = I_MYSQL_PORT
        super().__init__(self.host, self.user, self.passwd, self.dbname, self.port)


    def add_invoice(self, args):
        print('add_voice===values===:',args)
        # TODO: 处理插入异常
        self.insert('general_invoice', args,
                    "(invoice_code, invoice_number, invoice_data,"
                    "check_code, PurchaserRegisterNum, seller_register_num,GoodsServerName, "
                    "invoice_type, PurchaserName, AmountInWords,AmountInFiguers)"
                    )


    def get_rpa_exe(self, fields=None,condition=None):
        try:
            print(type(fields), fields)
            print(11)
            rpa_info = self.select(table = 'T_RPA_JOB', fields = fields, condition=condition);
            print(11)
            print('rpa_info ===============',rpa_info)
        except Exception  as e:
            rpa_info = '没有获取数据'
            print('数据获取失败',e)
        return rpa_info


    def get_invoice(self,):
        pass

    class Mysql_client(Mysql_base):
        ''' TODO 与业务有关的数据库操作方法'''

        def __init__(self):
            self.host = I_MYSQL_HOST
            self.user = I_MYSQL_USERNAME
            self.passwd = I_MYSQL_PASSWORD
            self.dbname = I_MYSQL_DATABASE_NAME
            self.port = I_MYSQL_PORT
            super().__init__(self.host, self.user, self.passwd, self.dbname, self.port)

        def add_invoice(self, args):
            print('add_voice===values===:', args)
            # TODO: 处理插入异常
            self.insert('general_invoice', args,
                        "(invoice_code, invoice_number, invoice_data,"
                        "check_code, PurchaserRegisterNum, seller_register_num,GoodsServerName, "
                        "invoice_type, PurchaserName, AmountInWords,AmountInFiguers)"
                        )

        def get_rpa_exe(self, filed=None):
            try:
                print(type(filed), filed)
                print(11)
                rpa_info = self.select(table='T_RPA_JOB', filed=filed);
                print(11)
                print('rpa_info ===============', rpa_info)
            except:
                rpa_info = '没有获取数据'
            return rpa_info

        def get_invoice(self, ):
            pass

    #  TODO  查询 远程FRM数据库的信息  回写咱们的数据库


# TODO     FRM数据交互
class Mysql_client_FRM(Mysql_base):
    ''' TODO 与业务有关的数据库操作方法'''

    def __init__(self):
        self.host = FRM_MYSQL_HOST_ALI
        self.user = FRM_MYSQL_USERNAME_ALI
        self.passwd = FRM_MYSQL_PASSWORD_ALI
        self.dbname = FRM_MYSQL_DATABASE_NAME_ALI
        self.port = FRM_MYSQL_PORT_ALI
        self.conn = self.connect()
        super().__init__(self.host, self.user, self.passwd, self.dbname, self.port)

    def get_select_one(self, sql_info):
        try:
            print(">>>>>>>>>>>>>>>>>>>>>>",sql_info)
            purchase_id  = self.select_one(sql_info)
            print('查询请购信息表id===:',purchase_id)
            return   purchase_id
        except Exception as e:
            print('没有id请从1开始',e )
            return False
        # TODO: 处理插入异常



    def get_select_all(self,sql_info):
        try:
            print(">>>>>>>>>>>>>>>>>>>>>>")
            purchase_id  = self.select_all(sql_info)
            print('查询请购信息表id===:',purchase_id)
            return   purchase_id
        except Exception as e:
            print('没有id请从1开始',e )
            return False
        # TODO: 处理插入异常


    def get_insert(self,table,values,fields=None):
        try:
            self.insert(table, values, fields)
        except Exception as e:
            print(e)

    def get_update(self, table, assignments, condition):
        try:
            self.update(table, assignments, condition)
            print('更新语句执行成功！！')
            return True
        except Exception as e:
            print('更新语句执行失败！！', e)
            return False



    def get_rpa_exe(self, filed=None):
        try:
            print(type(filed), filed)
            print(11)
            rpa_info = self.select(table='T_RPA_JOB', filed=filed);
            print(11)
            print('rpa_info ===============', rpa_info)
        except:
            rpa_info = '没有获取数据'
        return rpa_info

    def get_invoice(self, ):
        pass


'''
 机器人使用的编码
select business_type,job_id,purchase_time,applicant,procurement_type, goods_number,goods_count, recommended_unite_price_, recommended_date from purchase_apply_table as A inner join (select job_id from job_list_summary where job_status='1110' and user_name_id= (select user_name from user where user_agent_no = 'HipWang@081F7119C459')) as B on A.purchase_number=B.job_id

'''
