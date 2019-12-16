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
    #原来测试用的一些内容
    path('test/',views.test),   #这个是进行的多层匹配的一个测试
    path('main/',views.main),
    path('mywebsite/',views.index),
    path('search/',views.search),
    path('search2/',views.search2),
    path('auto_flash/',views.auto_flush),
    path('createregisterinfo/',views.RawVInfoRegisterview),

    # 关于index 下的所有的跳转的内容，都写在这个地方
    path('index/',views.index),
    path('index/dataview.html',views.dataviewredirect),

    # 所有关于dataview下的跳转的内容都写在下面
    path('dataview/',views.dataview),
    path('dataview/index.html',views.indexredirect)
    # 所有关于team 的跳转

    #所有关于contact 的跳转

    #所有关于 about 的跳转






    #所有关于da
]
