#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/20 18:17
# @Author : 黄林杰
# @File : views.py
# @Software: PyCharm

from django.http import HttpResponse

def index(request):
    html = '<h1>hello world</h1>'
    return HttpResponse(html)