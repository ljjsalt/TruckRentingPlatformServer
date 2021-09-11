import os
import sqlite3
from resources.database.pathinfo import *

'''
item [column1, column2, ...]
content {"key1":"value1", "key2":"value2"}
condition (key, value)
'''


# ['a','b'] -> 'a,b'
def accio_item(item):
    if item:
        comma = ','
        return comma.join(item)
    else:
        return '*'


def format_values(values):
    new = []
    for value in values:
        if isinstance(value, int):
            new.append(str(value))
        else:
            new.append('"'+value+'"')
    return new


def accio_condition(condition):
    if condition:
        key = condition[0]
        value = condition[1]
        if isinstance(value, int):
            v = str(value)
        else:
            v = '\"%s\"' % value
        return " WHERE %s = %s" % (key, v)
    else:
        return ""


def split_content(content):
    k = []
    v = []
    for key in content:
        k.append(key)
        v.append(content[key])
    return k, v


def execute(cr, code):
    if hasattr(cr, 'execute') & hasattr(cr, 'fetchall'):
        cr.execute(code)
        return cr.fetchall()


def executemany(cr, code):
    if hasattr(cr, 'executemany'):
        cr.executemany(code)


def executescript(cr, code):
    if hasattr(cr, 'executescript'):
        cr.executescript(code)


class LTDatabase(object):

    ways = {
        "ONE": execute,
        "MANY": executemany,
        "SCRIPT": executescript,
    }


    sql_initial_uri = db_initial()
    sql_backup_uri = db_backup()
    sql_create_uri = db_create()
    db_uri = db_main()

    def __init__(self, _type):
        self.type = _type

    def execute(self, code, way):
        rv = sqlite3.connect(self.db_uri)
        cr = rv.cursor()
        away = self.ways[way]
        info = away(cr, code)
        cr.close()
        rv.commit()
        rv.close()
        return info

    def init_db(self):
        with open(self.sql_initial_uri, 'r') as f:
            code = f.read()
            self.execute(code, 'SCRIPT')

    def create_db(self):
        with open(self.sql_create_uri, 'r') as f:
            code = f.read()
            self.execute(code, 'SCRIPT')

    def save_db(self):
        rv = sqlite3.connect(self.db_uri)
        with open(self.sql_backup_uri, 'w') as f:
            for line in rv.iterdump():
                f.write('%s\n' % line)

    def get_info(self, item, condition=0):
        demand = accio_item(item)
        cd = accio_condition(condition)
        command = 'SELECT %s FROM %s%s;' % (demand, self.type, cd)
        return self.execute(command, 'ONE')

    def add_info(self, content):
        key, value = split_content(content)
        keys = '(%s)' % accio_item(key)
        values = format_values(value)
        values = '(%s)' % accio_item(values)
        command = 'INSERT INTO %s %s VALUES %s;' % (self.type, keys, values)
        self.execute(command, 'ONE')

    def set_info(self, content, condition):
        key, value = split_content(content)
        sets = []
        for i in range(len(key)):
            sets.append("%s=\"%s\"" % (key[i], value[i]))
        _set = accio_item(sets)
        cd = accio_condition(condition)
        command = 'UPDATE %s SET %s%s;' % (self.type, _set, cd)
        self.execute(command, 'ONE')

    def has_info(self, condition):
        return self.get_info(0, condition)

    # !!!
    def del_info(self, _id):
        pass



if __name__ == '__main__':
    pass
    db = LTDatabase('GOOD')
    db.add_info({'ID':1000000001,'USERID':1,'DRIVERID':1, 'START_TIME':"2010年10月",'END_TIME':"2010年12月",'REMARK':'老司机666'})



