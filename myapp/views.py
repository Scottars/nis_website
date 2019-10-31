from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

'''
一个实现实时数据到界面上的方案：

'''


def test(request):
    mycontext={
        "my_text":"this is about us",
        "my_number":123
    }
    return render(request,"test.html",mycontext)

