from django.contrib import admin

from .models import Question

# Register your models here.

"""
「はじめてのDjangoアプリ作成、その2」にて追加
modelをadmin上で編集できるようにする
"""

admin.site.register(Question)