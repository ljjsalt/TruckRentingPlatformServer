import os

db_name = 'database.db'
backup_name = 'backup.sql'
initial_name = 'ltdb.sql'
create_name = 'LTDB.sql'
img = 'img'

def src_dir():
    return os.path.dirname(os.path.realpath(__file__)) + os.path.sep


def code_dir():
    return os.path.dirname(src_dir())


def db_main():
    return src_dir() + db_name


def db_backup():
    return src_dir() + backup_name


def db_initial():
    return src_dir() + initial_name


def db_create():
    return src_dir() + create_name

def img_dir():
    return src_dir() + img + os.path.sep


if __name__ == '__main__':
    print(db_main())
    print(db_backup())
    print(db_initial())
    print(db_create())
    print(img_dir())
