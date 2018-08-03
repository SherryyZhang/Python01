# -*- coding: utf-8 -*-
import sqlite3

# ���ӵ�SQLite���ݿ�
# ���ݿ��ļ���test.db
# ����ļ������ڣ����Զ��ڵ�ǰĿ¼����:
conn = sqlite3.connect('test.db')
# ����һ��Cursor:
cursor = conn.cursor()
# ִ��һ��SQL��䣬����user��:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# ����ִ��һ��SQL��䣬����һ����¼:
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# ͨ��rowcount��ò��������:
print('rowcount =', cursor.rowcount)
# �ر�Cursor:
cursor.close()
# �ύ����:
conn.commit()
# �ر�Connection:
conn.close()

# ��ѯ��¼��
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# ִ�в�ѯ���:
cursor.execute('select * from user where id=?', '1')
# ��ò�ѯ�����:
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

# -*- coding:utf-8 -*-
import salite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('ceate table user(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print('rowcount = ', cursor.rowcount)
cursor.close()
conn.commit()
conn.close()