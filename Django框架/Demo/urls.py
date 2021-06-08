# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import main

urlpatterns = [
    # URL映射 demo/json_demo
    url(r'^json_demo$', main.json_demo),
    # URL映射 demo/text_demo
    url(r'^text_demo$', main.text_demo),
    # URL映射 demo/html_demo
    url(r'^html_demo$', main.html_demo),
]
