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
app_name='myapp'
urlpatterns = [
    #原来测试用的一些内容
    path('test/',views.test),   #这个是进行的多层匹配的一个测试
    path('main/',views.main),
    path('mywebsite/',views.index),
    path('search/',views.search),
    path('search2/',views.search2),
    path('auto_flash/',views.auto_flush),
    path('createregisterinfo/',views.RawVInfoRegisterview),
##关于上面这个name的作用，可以在html中直接实现访问该链接，将该链接添加到ip：port/后面



    #注册登录相关
    path('registeraaaa/',views.registersave,name='register'),
    path('login/log',views.login,name='login'),
    path('logout/',views.logout),

    # 关于index 下的所有的跳转的内容，都写在这个地方
    path('index/',views.index),
    path('index/dataview.html',views.dataviewredirect),


    # 所有关于dataview下的跳转的内容都写在下面
    path('dataview/',views.dataview,name='dataview'),
    path('dataview/index.html',views.indexredirect),
    path ('dataview/getdata',views.dataviewsearch,name='datasearch'),


    #历史数据功能下载
    path('dataview/data_download/',views.data_download,name='data_download'),
    path('dataview/file_download/', views.big_file_download, name='file_download'),
    path('dataview/excel_export/', views.Export_excel, name='excel_export'),
    path('dataview/excel_download/', views.excel_download, name='excel_download'),

    #进程功能更新
    path('dataview/process_status_update/', views.process_status_update, name='process_status_update'),


    # 所有关于team 的跳转

    #所有关于contact 的跳转

    #所有关于 about 的跳转






    #所有关于da
]
