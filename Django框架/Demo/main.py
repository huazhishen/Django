# -*- coding: utf-8 -*-
from helper.http_helper import json_response
from helper.http_helper import text_response
from django.shortcuts import render_to_response as render
from . import logic


def json_demo(request):
    """
    接受请求
    """
    return json_response(logic.info(request))


def text_demo(request):
    """
    接受请求
    """
    return text_response(logic.info(request))


def html_demo(request):
    """
    接受请求
    """
    return render('index.html', context=logic.info(request))
