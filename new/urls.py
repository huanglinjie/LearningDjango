#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 00:12
# @Author  : 黄林杰
# @File    : urls.py
# @Software: PyCharm

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]
