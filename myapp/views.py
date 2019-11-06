from django.shortcuts import render
from django.http import HttpResponse

from .models import VInfoRegister
from .forms import VInforRegister_form

'''
一个实现实时数据到界面上的方案：

'''


def  VInfoRegisterview(request):
    form = VInforRegister_form(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form

    }
    return  render(request,'register_info_create.html',context)




def test(request):

    s=VInfoRegister.objects.all()

    mycontext={
        "my_text":"this is about us",
        "my_number":123,
        "register":s
    }


    return render(request,"test.html",mycontext)


def main(request):
    return render(request,'main.html')

def search(request):
    a=VInfoRegister.objects.all()[0:2]


    print('hello world')
    my_data={
        'name':request.POST['q'],
        'value':12.5,
        'VRegisterInfo':a
    }
    return render(request,'main.html',my_data)
    # return HttpResponse('name')  #这个相当于一个简易的界面，直接进行跳转的


def search2(request):
    a = VInfoRegister.objects.all()[0:1]

    print('hello world')
    my_data = {
        'name2':'hha',
        'value2':14.25,
        'VRegisterInfo': a
    }
    print('this ia  a bnew')
    return render(request, 'main.html', my_data)
def auto_flush(request):
    # return render(request,'main.html')
    return HttpResponse('我们点击了这个按钮')