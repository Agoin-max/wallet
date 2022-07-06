import logging
from django.db import connections
from collections import OrderedDict

logger = logging.getLogger(__name__)

DEFAULT_DB = 'default'


def select_dict(sql, params=None, db=DEFAULT_DB, flat=False):
    """ Return one/all rows from a cursor as a dict """
    if not sql:
        if flat:
            return {}
        else:
            return []
    if not db:
        db = DEFAULT_DB
    with connections[db].cursor() as cursor:
        try:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            if flat:
                fetchone = cursor.fetchone()
                if fetchone:
                    return dict(zip(columns, fetchone))
                else:
                    return {}
            else:
                return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except (Exception,):
            logger.debug('dict sql :' + sql + '; params:' + str(params))
            if flat:
                return {}
            else:
                return []


def select_list(sql, params=None, db=DEFAULT_DB, flat=False):
    """ Return one/all rows from a cursor as a list """
    if not sql:
        return []
    if not db:
        db = DEFAULT_DB
    with connections[db].cursor() as cursor:
        try:
            cursor.execute(sql, params)
            if flat:
                fetchone = cursor.fetchone()
                if fetchone:
                    return list(fetchone)
                else:
                    return []
            else:
                return [list(row) for row in cursor.fetchall()]
        except (Exception,):
            logger.debug('list sql :' + sql + '; params:' + str(params))
            return []


def wallet_execute(sql, params=None, db=DEFAULT_DB, is_insert=False):
    if not sql:
        return None
    if not db:
        db = DEFAULT_DB
    with connections[db].cursor() as cursor:
        try:
            cursor.execute(sql, params)
            if is_insert:
                return cursor.lastrowid
        except (Exception,):
            logger.debug('execute sql -> ' + sql + '; params -> ' + str(params))
            return


def get_pagination_data(sql, total_sql, order_by='', page=1, pagesize=20, params=None, db=DEFAULT_DB):
    """ 分页函数 """
    page = int(page)
    page = 1 if page < 1 else page

    pagesize = int(pagesize)
    pagesize = 0 if pagesize < 1 else pagesize

    if order_by:
        sql += " order by {order_by} ".format(order_by=order_by)
    sql += " limit {start}, {pagesize} ".format(start=(page - 1) * pagesize, pagesize=pagesize)
    results = select_dict(sql, params=params, db=db)
    count = select_dict(total_sql, params=params, flat=True, db=db)

    return OrderedDict([
        ('count', count['count']),
        ('pagenum', page),
        ('pagesize', pagesize),
        ('records', results),
    ])
