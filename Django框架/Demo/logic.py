# -*- coding: utf-8 -*-
from helper import mysql_helper


def info(request):
    """
    这里处理业务逻辑
    """
    return {
        "demo1": "Hello World!!!",
        "request": request
    }


def create(request):
    """
    这里处理业务逻辑
    """
    dao = mysql_helper.mysql_base()
    dao.insertData("demo_model", {"name": "测试一", "code": "ceshi1"})
    return "create success"


def edit(request):
    """
    这里处理业务逻辑
    """
    dao = mysql_helper.mysql_base()
    dao.updateData("demo_model", {"name": "测试一_edit", "code": "ceshi1_edit"}, {"id=": 1})
    return "edit success"


def delete(request):
    """
    这里处理业务逻辑
    """
    dao = mysql_helper.mysql_base()
    dao.deleteData("demo_model", {"id=": 2})
    return "delete success"


def search(request):
    """
    这里处理业务逻辑
    """
    dao = mysql_helper.mysql_base()
    data = dao.selectData("demo_model", {"id=": 1})
    print data
    return "search success"
