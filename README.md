# hoo


创建数据库
----------
    mysql> CREATE DATABASE wallet DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

    mysql> create user wallet@'localhost' identified by 'wallet';

    mysql> grant all privileges on wallet.* to wallet@localhost identified by 'wallet';

    mysql> flush privileges;

    mysql 8.0 修改权限
    mysql> CREATE USER 'wallet'@'%' IDENTIFIED BY 'wallet';
    mysql> GRANT ALL ON *.* TO 'wallet'@'%' WITH GRANT OPTION;
    修改密码
    mysql> ALTER USER 'root'@'127.0.0.1' IDENTIFIED WITH mysql_native_password BY 'password';

更新语言包
------
    settings:
    LANGUAGES = (
        ('zh-hans', '简体中文'),
        ('zh-hant', '繁体中文'),
        ('en', 'English'),
        ('ko', '韩语'),
        ('ja', '日语'),
    )
    LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale/'),)
    LANGUAGE_COOKIE_NAME = 'django_language'
    LANGUAGE_SESSION_KEY = '_language'
    
    创建语言文件（中文的语言包生成时要用下划线）
    python manage.py makemessages -l en --ignore=admin.py --ignore=apps.py
    python manage.py makemessages -l zh_Hans --ignore=admin.py --ignore=apps.py
    python manage.py makemessages -l zh_Hant --ignore=admin.py --ignore=apps.py
    python manage.py makemessages -l ko --ignore=admin.py --ignore=apps.py
    python manage.py makemessages -l ja --ignore=admin.py --ignore=apps.py
    
    编译语言文件
    python manage.py compilemessages -l en
    python manage.py compilemessages -l zh_Hans
    python manage.py compilemessages -l zh_Hant
    python manage.py compilemessages -l ko
    python manage.py compilemessages -l ja
