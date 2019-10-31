from django.contrib import admin
from django.urls import path,include


#整体的过程：
'''
1、web 请求nis_website 下的urls
2、由于include 在匹配了一部分那个地方的url的时候会跳转到include内的部分
3、然后后面的东西继续进行匹配，然后如果匹配则调用views  也就是视图函数，
4、视图函数可以直接给返回相映，也可以通过render 来调用实际的html 页码来实现
'''

from . import views
urlpatterns = [
    path('test/',views.test)   #这个是进行的多层匹配的一个测试
]
