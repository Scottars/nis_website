from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import VInfoRegister,NisUserInfo
from .forms import VInforRegister_form,RawVinforresiger_form,NisUserInfo_form,RawUserInfo_form

# class Registertest(View):
#     def get(self, request):
#         # 表单渲染注册界面
#         form = RegisterForm()
#         return render(request, 'mywebsite/register_2.html',context={
#             'form':form,
#         })
#     def post(self, request):
#         # 表单校验数据
#         form = RegisterForm(request.POST)
#         # 如果数据正确
#         if form.is_valid():
#             return HttpResponse('注册成功')
#
#         # 若校验失败，则渲染注册界面
#         return render(request, 'mywebsite/register_2.html', context={
#             'form': form,
#         })
#

##能够直接form.forms的表单进行
def register(request):
    my_form = NisUserInfo_form(request.GET)
    print('we are hehre')
    if request.method == "POST":
        my_form = RawUserInfo_form(request.GET)
    context = {
        'form':my_form

    }
    return  render(request,'mywebsite/register_2.html',context)
def  registersave(request):
    form = NisUserInfo_form(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form,

    }
    return  render(request,'mywebsite/register_2.html',context)





def login(request):

    return render(request,'mywebsite/login.html')

    pass
def checkPassword(cp,pwd):
    list = VInfoRegister.objects.filter(phone = cp,password = pwd)
    print('查询结果:',list)
    if len(list)==0:
        print()
        return False
    else:
        return True



    pass
















'''
一个实现实时数据到界面上的方案：

'''
def  RawVInfoRegisterview(request):
    my_form = RawVinforresiger_form(request.GET)
    if request.method == "POST":
        my_form = RawVinforresiger_form(request.POST)
    context = {
        'form':my_form

        }
    return  render(request, '../static/../templates/mywebsite/register_info_create.html', context)


#
# def  VInfoRegisterview(request):
#     form = VInforRegister_form(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form':form
#
#     }
#     return  render(request,'register_info_create.html',context)




def test(request):

    s=VInfoRegister.objects.all()

    mycontext={
        "my_text":"this is about us",
        "my_number":123,
        "register":s
    }


    return render(request,"test.html",mycontext)


def main(request):
    return render(request, 'main.html')
def index(request):
    return render(request, 'mywebsite/index.html')
def dataview(request):
    # return HttpResponseRedirect("dataview/")
    return render(request, 'mywebsite/dataview.html')
def dataviewredirect(request):  #从头开始跳转
    return HttpResponseRedirect("/dataview/")
    # return render(request, 'mywebsite/dataview.html')

def teststatic(request):
    return render(request, 'mywebsite/teststatic.html')
def indexredirect(request):  #从头开始跳转
    return HttpResponseRedirect("/index/")
    # return render(request, 'mywebsite/dataview.html')



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